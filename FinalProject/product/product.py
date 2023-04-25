from flask import Blueprint, render_template, flash, redirect, url_for, current_app, session, request
from auth.forms import LoginForm, RegisterForm, ProfileForm
from sql.db import DB
from flask_login import login_required, current_user
from roles.permissions import product_permission
from product.forms import ProductAdd

product = Blueprint('product', __name__, url_prefix='/product',template_folder='templates')


@product.route("/add", methods=["GET","POST"])
@login_required
@product_permission.require(http_exception=403)
def add():
    form = ProductAdd()
    title = "Add"
    if form.validate_on_submit():
        try:
            productName = form.productName.data
            productDesc = form.productDesc.data
            productCategory = form.productCategory.data
            stock = form.stock.data
            unitprice = form.unitprice.data
            visibility = 0
            if form.visibility.data == True:
                visibility = 1
            result = DB.insertOne("""INSERT INTO IS601_Product (product_name, prodct_description, category, stock, unit_price, visibility) 
                    VALUES (%s,%s,%s,%s,%s,%s)""", productName, productDesc, productCategory, stock, unitprice, visibility)
            if result.status:
                flash("New Product Added", "success")
                form = ProductAdd()
        except Exception as e:
            flash("Something wen't wrong, please try again later", "danger")
    return render_template('product_add.html', form=form, title=title)

@product.route("/edit", methods=["GET","POST"])
@login_required
@product_permission.require(http_exception=403)
def edit():
    form = ProductAdd()
    try:
        id = request.args['id']
    except:
        id = ""
    if form.validate_on_submit() and request.method == "POST":
        productName = form.productName.data
        productDesc = form.productDesc.data
        productCategory = form.productCategory.data
        stock = form.stock.data
        unitprice = form.unitprice.data
        visibility = 0
        if form.visibility.data == True:
            visibility = 1
        result = DB.update("""UPDATE IS601_Product set product_name = %s, prodct_description = %s, category = %s, stock = %s, unit_price = %s, visibility = %s where id = %s""", 
                           productName, productDesc, productCategory, stock, unitprice, visibility, id) 
        flash("Product Updated Successfully", "success")
    if id != "":
        results = DB.selectOne("""
                                    SELECT id, product_name, prodct_description, category, stock, unit_price, visibility
                                    FROM IS601_Product
                                    where id = %s;
                               """, id)
        if results.status and results.row:
            form.productName.data = results.row['product_name']
            form.productDesc.data = results.row['prodct_description']
            form.productCategory.data = results.row['category']
            form.stock.data = results.row['stock']
            form.unitprice.data = results.row['unit_price']
            form.visibility.data = True if results.row['visibility'] else False
            form.submit.label.text = "Edit Product"
    else:
        return redirect(url_for('product.view'))
    return render_template('product_add.html', form=form, title="Edit")

@product.route("/viewAdmin", methods=["GET","POST"])
@login_required
@product_permission.require(http_exception=403)
def viewAdmin():
    results = []
    args = {}

    '''
        UCID - dm767
        Date - April 24, 2023
    '''

    query = """
                SELECT id, product_name, prodct_description, category, stock, unit_price, visibility
                FROM IS601_Product
                where 1=1
            """
    limit = 10 # TODO change this per the above requirements
    if request.args.get('product_name'):
        name = request.args.get('product_name')
        query += " and product_name like %(name)s"
        args['name'] = "%"+name+"%"
    if request.args.get('category'):
        category = request.args.get('category')
        query += " and category = %(category)s"
        args['category'] = category
    if request.args.get('order') and request.args.get('order') != "":
        order = request.args.get('order')
        getType = request.args.get('type')
        query += f" order by {order} {getType}"
    query += " LIMIT %(limit)s"
    args["limit"] = limit
    try:
        results = DB.selectAll(query, args)
        if results.status and results.rows:
            results = results.rows
    except Exception as e:
        print(str(e))
    return render_template('product_view.html', rows=results)

@product.route("/view", methods=["GET","POST"])
@login_required
def view():
    results = []
    args = {}

    '''
        UCID - dm767
        Date - April 24, 2023
    '''

    query = """
                SELECT id, product_name, prodct_description, category, stock, unit_price
                FROM IS601_Product
                where 1=1 and visibility = 1
            """
    limit = 10 # TODO change this per the above requirements
    if request.args.get('product_name'):
        name = request.args.get('product_name')
        query += " and product_name like %(name)s"
        args['name'] = "%"+name+"%"
    if request.args.get('category'):
        category = request.args.get('category')
        query += " and category = %(category)s"
        args['category'] = category
    if request.args.get('order') and request.args.get('order') != "":
        order = request.args.get('order')
        getType = request.args.get('type')
        query += f" order by {order} {getType}"
    query += " LIMIT %(limit)s"
    args["limit"] = limit
    try:
        results = DB.selectAll(query, args)
        if results.status and results.rows:
            results = results.rows
    except Exception as e:
        print(str(e))
    return render_template('product_view.html', rows=results)

@product.route("/product-view", methods=['GET'])
@login_required
def productview():
    try:
        id = request.args['id']
    except:
        id = ""
    if id != "":
        result = []
        try:
            result = DB.selectOne("""
                                        SELECT id, product_name, prodct_description, category, stock, unit_price
                                        FROM IS601_Product
                                        where id = %s
                                 """, id)
            print(result)
        except Exception as e:
            print(str(e))
        return render_template('product_single_view.html', row=result.row)
    else:
        return redirect(url_for('product.view'))

@product.route("/add-to-cart", methods=['GET'])
@login_required
def addToCart():
    try:
        id = int(request.args['id'])
    except:
        id = ""
    try:
        quantity = int(request.args['quantity'])
    except:
        quantity = 1
    customer_id = int(current_user.get_id())
    if id != "":
        try:
            # result = DB.selectOne("""
            #                             SELECT id, product_name, prodct_description, category, stock, unit_price
            #                             FROM IS601_Product
            #                             where id = %s
            #                      """, id)

            result = DB.selectOne("""
                                        SELECT id, quantity from IS601_CART where customer_id = %s and product_id = %s
                                    """, customer_id, id)
            if result.status and result.row:
                quantity += int(result.row['quantity'])
                result = DB.update("""
                                        UPDATE IS601_CART set quantity = %s where customer_id=%s and product_id=%s
                                    """, quantity, customer_id, id)
                flash("Product Updated in Cart", "success")
            else:
                result = DB.insertOne("""
                                        INSERT into IS601_CART(customer_id, product_id, quantity) VALUES(%s, %s, %s)
                                    """, customer_id, id, quantity)
                flash("Product Added in Cart", "success")
        except Exception as e:
            print(str(e))
            flash("Something wen't wrong, please try again later", "danger")
        return redirect(url_for('product.view'))
    else:
        return redirect(url_for('product.view'))

@product.route("/view-cart", methods=['GET','POST'])
@login_required
def viewCart():
    results = []
    if request.method == "POST":
        quantity = int(request.form.get('quantity'))
        cart_id = int(request.form.get('cart_id'))
        if quantity <= 0:
            result = DB.delete("DELETE FROM IS601_CART where id = %s", cart_id)
            if result.status:
                flash("Deleted item from cart", "success")
        else:
            result = DB.update("""UPDATE IS601_CART set quantity = %s where id=%s """, quantity, cart_id)
            flash("Product Updated in Cart", "success")
    try:
        user_id = int(current_user.get_id())
        results = DB.selectAll("""
                                    SELECT C.id as cart_id, C.product_id, C.quantity, P.product_name, P.unit_price
                                    FROM IS601_CART as C
                                    LEFT JOIN IS601_Product as P on P.id = C.product_id
                                    where C.customer_id = %s
                               """, user_id)
        if results.status and results.rows:
            for row in results.rows:
                row['total_price'] = int(row['quantity']) * float(row['unit_price'])
            results = results.rows
        else:
            results = []
    except Exception as e:
        print(str(e))
        flash("Something wen't wrong, please try again later", "danger")
    return render_template("cart_view.html", rows=results)

@product.route('/clear-cart', methods=['GET'])
@login_required
def clearcart():
    id = current_user.get_id()
    result = DB.delete("""
                            DELETE FROM IS601_CART where customer_id = %s
                        """, id)
    return redirect(url_for('product.viewCart'))