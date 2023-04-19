from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional, InputRequired
from wtforms.validators import ValidationError

def is_valid_username(username):
    import re
    r = re.fullmatch("^[a-zA-Z0-9_-]{2,30}$", username)
    if not r:
        raise ValidationError("Invalid username format, username can contains only alphabets and numerics with _ or -")

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = EmailField("email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[InputRequired()])
    submit = SubmitField("Login")

class ProfileForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    username = StringField("Username", validators=[DataRequired()])
    oldpassword = PasswordField("Old Password", validators=[Optional(), Length(8)])
    newpassword = PasswordField("New Password", validators=[Optional(), EqualTo('confirmnew', message='Passwords and Confirm Password aren\'t same'), Length(8)])
    confirmnew = PasswordField("Confirm New Password", validators=[Optional(),  EqualTo('newpassword', message='Passwords and Confirm Password aren\'t same'),Length(8)])
    submit = SubmitField("Update Profile")
    def validate_username(form, field):
        is_valid_username(field.data)