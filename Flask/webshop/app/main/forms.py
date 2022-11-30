from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError, EqualTo, Length
from app.models import User


class UpdateItemForm(FlaskForm):
    amount = StringField("Amount")
    submit = SubmitField("Update basket")


class BuyItemForm(FlaskForm):
    amount = StringField("Amount")
    submit = SubmitField("Add to basket")


def DynamicForm(*args, **kwargs):
    class StaticFrom(FlaskForm):
        submit = SubmitField("Continue to checkout")

    for i in args[0]:
        setattr(
            StaticFrom, 
            f"feild_quant_{i.item_id}", 
            StringField(f"None{i.item_id}")
        )
    
    return StaticFrom
