from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, HiddenField, IntegerField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Email, ValidationError, EqualTo, Length
from app.models import User


class UpdateItemForm(FlaskForm):
    amount = StringField("Amount")
    submit = SubmitField("Update basket")


class BuyItemForm(FlaskForm):
    amount = StringField("Amount")
    submit = SubmitField("Add to basket")


class CuponForm(FlaskForm):
    code = StringField("Cupon Code")
    submit = SubmitField("Apply")


def DynamicForm(*args, **kwargs):
    class StaticFrom(FlaskForm):
        submit = SubmitField("Continue to checkout")

    for i in args[0]:
        setattr(
            StaticFrom, 
            f"feild_quant_{i.item_id}", 
            IntegerField(f"None{i.item_id}", validators=[NumberRange(min=0, max=100)])
        )
        setattr(
            StaticFrom,
            f"feild_hidden_{i.id}",
            HiddenField(f"None{i.id}")
        )
    
    return StaticFrom
