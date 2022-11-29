from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError, EqualTo, Length
from app.models import User, Question, Awnser, Choice


def DynamicQuestionForm(*args, **kwargs):
    class StaticFrom(FlaskForm):
        submit = SubmitField("Indsend")

    for q in Question.query.all():
        if q.type == "StringField":
            setattr(StaticFrom, f"feild_StringField_{q.id}", StringField(q.body, validators=[Length(max=50)]))
        elif q.type == "SelectField":
            choices = [i.body for i in q.choices.all()]
            setattr(StaticFrom, f"feild_SelectField_{q.id}", SelectField(q.body, choices=choices))
    
    return StaticFrom
