from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField, SelectField, BooleanField, IntegerField, DecimalField
from wtforms.validators import DataRequired, Length, Optional, InputRequired
from wtforms.validators import ValidationError

class ProductAdd(FlaskForm):
    productName = StringField("Product Name", validators=[DataRequired()])
    productDesc = TextAreaField("Product Description", validators=[DataRequired()])
    productCategory = SelectField('Category', choices=[('book','Book'),('food','Food'),('electronics','Electonics')])
    stock = IntegerField("Stock", validators=[DataRequired()])
    unitprice = DecimalField("Price", validators=[DataRequired()])
    visibility = BooleanField("Visible", validators=[Optional()])
    submit = SubmitField("Add Product")

class PurchaseCheckout(FlaskForm):
    firstName = StringField("First Name", validators=[DataRequired()])
    lastName = StringField("Last Name", validators=[DataRequired()])
    streetaddress1 = StringField("Street Address 1", validators=[DataRequired()])
    streetaddress2 = StringField("Street Address 2")
    state = SelectField("State", choices=[('NJ','New Jersey'),('NY','New York'), ('MA','Massachusetts'),('AZ','Arizona')])
    city = StringField("City", validators=[DataRequired()])
    country = StringField("Country", validators=[DataRequired()])
    zipcode = StringField("Zip Code", validators=[DataRequired()])
    modeofpayment = SelectField("Mode Of Payment", choices=[('cod','Cash on Deilvery'),('debit','Debit Card'), ('credit','Credit Card'),('paypal','Paypal')])
    price = DecimalField("Enter Amount", validators=[DataRequired()])
    submit = SubmitField("Purchase")