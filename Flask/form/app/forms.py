from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError, EqualTo
from app.models import User, Question, Awnser, Choice

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField("Repeat Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')


class AdminAddForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    type = SelectField("Type", choices=["StringField", "SelectField"])
    submit = SubmitField('Tilføj')


class AdminEditSelectForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])

    feild1 = StringField("Feild 1", validators=[])
    feild2 = StringField("Feild 2", validators=[])
    feild3 = StringField("Feild 3", validators=[])
    feild4 = StringField("Feild 4", validators=[])

    submit = SubmitField('Gem')


def DynamicQuestionForm(*args, **kwargs):
    class StaticFrom(FlaskForm):
        submit = SubmitField("Indsend")

    for q in Question.query.all():
        if q.type == "StringField":
            setattr(StaticFrom, f"feild_StringField_{q.id}", StringField(q.body))
        elif q.type == "SelectField":
            choices = [i.body for i in q.choices.all()]
            setattr(StaticFrom, f"feild_SelectField_{q.id}", SelectField(q.body, choices=choices))
    
    return StaticFrom



