from flask import Blueprint, render_template, flash, redirect, url_for,current_app, session
from auth.forms import LoginForm, RegisterForm, ProfileForm
from sql.db import DB

from flask_login import login_user, login_required, logout_user, current_user
from auth.models import User
from flask_bcrypt import Bcrypt

from email_validator import validate_email

bcrypt = Bcrypt()

from flask_principal import Identity, AnonymousIdentity, identity_changed


auth = Blueprint('auth', __name__, url_prefix='/',template_folder='templates')


@auth.route("/register", methods=["GET","POST"])
def register():
    if current_user.is_active != False:
        return redirect(url_for('auth.dashboard'))
    form = RegisterForm()
    # wtform validators are both client-side and server-side
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data
        try:
            is_valid = True
            checkEmail = DB.selectOne("select * from IS601_Users where email = %s", email)
            if checkEmail.status and checkEmail.row:
                is_valid = False
                flash("Email Already Exists", "warning")
            checkUsername = DB.selectOne("select * from IS601_Users where username = %s", username)
            if checkUsername.status and checkUsername.row:
                is_valid = False
                flash("Username Already Exists", "warning")
            if is_valid:
                hash = bcrypt.generate_password_hash(password)
                # save the hash, not the plaintext password
                result = DB.insertOne("INSERT INTO IS601_Users (email, username, password) VALUES (%s, %s, %s)", email, username, hash)
                if result.status:
                    flash("Successfully registered","success")
        except Exception as e:
            flash(str(e), "danger")
    return render_template("register.html", form=form)

@auth.route("/", methods=["GET", "POST"])
def login():
    if current_user.is_active != False:
        return redirect(url_for('auth.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        is_valid = True
        if "@" in email:
            try:
                validate_email(email)
            except:
                is_valid = False
                flash("Invalid email address", "danger")
        else:
            import re
            r = re.fullmatch("/^[a-z0-9_-]{2,30}$/", email)
            if r:
                is_valid = False
                flash("Invalid username", "danger")
        password = form.password.data
        try:
            if is_valid:
                result = DB.selectOne("SELECT id, email, username, password FROM IS601_Users where email=%s", email)
                if result.status and result.row:
                    hash = result.row["password"]
                    if bcrypt.check_password_hash(hash, password):
                        from roles.models import Role
                        del result.row["password"] # don't carry password/hash beyond here
                        user = User(**result.row)
                        # get roles
                        result = DB.selectAll("""
                        SELECT name FROM IS601_Roles r JOIN IS601_UserRoles ur on r.id = ur.role_id WHERE ur.user_id = %s AND r.is_active = 1 AND ur.is_active = 1
                        """, user.id)
                        if result.status and result.rows:
                            user.roles = [Role(**r) for r in result.rows]
                        success = login_user(user) # login the user via flask_login
                        
                        if success:
                            # Tell Flask-Principal the identity changed
                            identity_changed.send(current_app._get_current_object(),
                                    identity=Identity(user.id))
                            # store user object in session as json
                            session["user"] = user.toJson()
                            flash("Log in successful", "success")
                            return redirect(url_for("auth.dashboard"))
                        else:
                            flash("Error logging in", "danger")
                    else:
                        flash("Invalid password", "warning")
                else:
                    flash("Invalid user", "warning")
        except Exception as e:
            flash(str(e), "danger")
    return render_template("login.html", form=form)

@auth.route("/dashboard", methods=["GET"])
@login_required
def dashboard():
    return render_template("landing_page.html")

@auth.route('/profile', methods=["GET", "POST"])
@login_required
def profile():
    user_id = current_user.get_id()
    form  = ProfileForm()
    if form.validate_on_submit():
        is_valid = True
        username = form.username.data
        email = form.email.data
        oldpassword = form.oldpassword.data
        newpassword = form.newpassword.data
        confirmnew = form.confirmnew.data
        flagged = False
        if oldpassword and newpassword and confirmnew:
            try:
                result = DB.selectOne("SELECT password FROM IS601_Users where id = %s", user_id)
                if result.status and result.row:
                    # verify current password
                    if bcrypt.check_password_hash(result.row["password"], oldpassword):
                        # update new password
                        hash = bcrypt.generate_password_hash(newpassword)
                        try:
                            result = DB.update("UPDATE IS601_Users SET password = %s WHERE id = %s", hash, user_id)
                            if result.status:
                                # logout_user()
                                # flash("Password updated, please login again", "success")
                                # return redirect(url_for("home.index"))
                                flagged = True
                        except Exception as e:
                            flash("We ran into some issue while updating password, please try again later", "danger")
                    else:
                        flash("Invalid password","danger")
            except Exception as e:
                flash(str(e), "danger")
        if is_valid:
            try: # update email, username (this will trigger if nothing changed but it's fine)
                try:
                    is_valid = True
                    checkEmail = DB.selectOne("select * from IS601_Users where email = %s", email)
                    if checkEmail.status and checkEmail.row:
                        is_valid = False
                        flash("Email Already Exists", "warning")
                    checkUsername = DB.selectOne("select * from IS601_Users where username = %s", username)
                    if checkUsername.status and checkUsername.row:
                        is_valid = False
                        flash("Username Already Exists", "warning")
                    if is_valid:
                        result = DB.update("UPDATE IS601_Users SET email = %s, username = %s WHERE id = %s", email, username, user_id)
                        if result.status and flagged:
                            flash("Profile Updated, please login again", "success")
                        else:
                            flash("Profile Updated" , "success")
                except Exception as e:
                    flash("Maybe the username is taken try something else.", "danger")
            except Exception as e:
                flash(e, "danger")
        if flagged:
            logout_user()
            return redirect(url_for("home.index"))
        else:
            try:
                result = DB.selectOne("SELECT id, email, username FROM IS601_Users where id = %s", user_id)
                if result.status and result.row:
                    user = User(**result.row)
                    current_user.email = user.email
                    current_user.username = user.username
            except Exception as e:
                flash(e, "danger")
    form.email.data = current_user.email
    form.username.data = current_user.username
    return render_template("profile.html", form=form)

@auth.route("/logout", methods=["GET"])
def logout():
    if current_user.is_active != False:
        logout_user()
        # Remove session keys set by Flask-Principal
        for key in ('identity.name', 'identity.auth_type'):
            session.pop(key, None)
        # Tell Flask-Principal the user is anonymous
        identity_changed.send(current_app._get_current_object(),
                            identity=AnonymousIdentity())
        flash("Successfully logged out", "success")
    return redirect(url_for("auth.login"))