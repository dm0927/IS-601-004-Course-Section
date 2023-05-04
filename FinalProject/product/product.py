from flask import Blueprint, render_template, flash, redirect, url_for, current_app, session, request
from sql.db import DB
from flask_login import login_required, current_user
from roles.permissions import product_permission
from product.forms import ProductAdd, PurchaseCheckout

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

@product.route('/purchase', methods=['GET','POST'])
@login_required
def purchase():
    form = PurchaseCheckout()  
    try:
        user_id = int(current_user.get_id())
        results = []
        results = DB.selectAll("""
                                    SELECT C.id as cart_id, C.product_id, C.quantity, P.product_name, P.unit_price
                                    FROM IS601_CART as C
                                    LEFT JOIN IS601_Product as P on P.id = C.product_id
                                    where C.customer_id = %s
                                """, user_id)
        
        if len(results.rows) <= 0:
            return redirect(url_for('product.viewCart'))
        
        if results.status and results.rows:
            for row in results.rows:
                row['total_price'] = int(row['quantity']) * float(row['unit_price'])
            results = results.rows


        '''
            UCID - dm767
            Date - May 4
        '''

        if form.validate_on_submit():
            firstName = request.form.get('firstName')
            lastName = request.form.get('lastName')
            streetaddress1 = request.form.get('streetaddress1')
            streetaddress2 = request.form.get('streetaddress2')
            state = request.form.get('state')
            city = request.form.get('city')
            country = request.form.get('country')
            zipcode = request.form.get('zipcode')
            modeofpayment = request.form.get('modeofpayment')
            price = float(request.form.get('price'))

            payment_method = ['cod','debit','credit','paypal']

            total_price = 0
            
            for row in results:
                total_price +=  row['total_price']
            
            validationApproved = True

            if modeofpayment not in payment_method:
                validationApproved = False
                flash("Incorrect Mode Of Payment, please enter a correct payment mode", "warning")
            
            if float(total_price) != price:
                validationApproved = False
                flash("Incorrect Amount, please enter a correct amount", "warning")
            
            for row in results:
                getProductQTYandPrice = DB.selectOne("""
                                            SELECT id, product_name, stock, unit_price
                                            FROM IS601_Product
                                            where id = %s
                                        """, row['product_id'])
            
                getProductQTYandPrice = getProductQTYandPrice.row
                if getProductQTYandPrice['stock'] - row['quantity'] < 0:
                    validationApproved = False
                    flash(f"{getProductQTYandPrice['product_name']} is out of stock.", "warning")
                if getProductQTYandPrice['unit_price'] != row['unit_price']:
                    validationApproved = False
                    flash(f"{getProductQTYandPrice['product_name']} price has been changed from {getProductQTYandPrice['unit_price']} to {row['unit_price']}.", "warning")

            if validationApproved:
                pass
                # Do Code of inserting data into database
                order_data = DB.insertOne("""
                                            INSERT INTO 
                                                        IS601_Orders(first_name, last_name, address, total_price, money_received, user_id, payment_method)
                                                        VALUES(%s, %s, %s, %s, %s, %s, %s)
                                          """, firstName, lastName, (streetaddress1 + " " + streetaddress2 + ", " + city + ", " + state + ", " + country + ", " + zipcode), total_price, total_price, user_id, modeofpayment)
                order_id = DB.selectOne("""
                                            SELECT LAST_INSERT_ID() as order_id;
                                        """)
                
                order_id = order_id.row['order_id']

                for row in results:
                    DB.insertOne("""
                                    INSERT INTO IS601_Orderitemss(order_id, product_id, quantity, price)
                                    VALUES(%s, %s, %s, %s)
                                 """, order_id, row['product_id'], row['quantity'], row['unit_price'])
                DB.delete("""DELETE FROM IS601_CART where customer_id = %s """, user_id)
                flash("Order Placed", "success")

                if modeofpayment == "cod":
                    modeofpayment = "Cash on Delivery"
                    textMOD = "Will Pay once the product are deliverd"
                elif modeofpayment == "debit":
                    modeofpayment = "Debit Card"
                    textMOD = "Paid via a debit card"
                elif modeofpayment == "credit":
                    modeofpayment = "Credit Card"
                    textMOD = "Paid via a credit card"
                elif modeofpayment == "paypal":
                    modeofpayment = "Paypal"
                    textMOD = "Paid via a paypal account"

                orderData = {
                    'firstname' : firstName,
                    'lastname' : lastName,
                    'address' : (streetaddress1 + " " + streetaddress2 + ", " + city + ", " + state + ", " + country + ", " + zipcode),
                    'total_price' : total_price,
                    'modeofpayment' : modeofpayment,
                    'textMOD': textMOD

                }

                return render_template("orderconfirmation.html", orderitemplaced=orderData, orderData=results)


    except Exception as e:
            print(str(e))
            flash("Something wen't wrong, please try again later", "danger")
    return render_template("purchase.html", form=form, rows=results)


@product.route('/view-orders', methods=['GET'])
@login_required
def customervieworder():
    try:
        user_id = int(current_user.get_id())
        result = []
        result = DB.selectAll("""
                                SELECT id, total_price, created
                                from IS601_Orders
                                where user_id = %s
                              """, user_id)
        if result.status:
            for row in result.rows:
                row['created'] = str(row['created'])
    except Exception as e:
        print(str(e))
        flash("Something wen't wrong, please try again later", "danger")

    return render_template("viewcustomerorder.html", rows=result.rows)


@product.route('/clear-cart', methods=['GET'])
@login_required
def clearcart():
    id = current_user.get_id()
    result = DB.delete("""
                            DELETE FROM IS601_CART where customer_id = %s
                        """, id)
    return redirect(url_for('product.viewCart'))