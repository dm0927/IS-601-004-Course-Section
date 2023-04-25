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