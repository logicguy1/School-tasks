from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User


class AdminAddForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=50)])
    type = SelectField("Type", choices=["StringField", "SelectField"])
    submit = SubmitField('Tilføj')


class AdminEditSelectForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=0, max=50)])

    feild1 = StringField("Feild 1", validators=[Length(max=50)])
    feild2 = StringField("Feild 2", validators=[Length(max=50)])
    feild3 = StringField("Feild 3", validators=[Length(max=50)])
    feild4 = StringField("Feild 4", validators=[Length(max=50)])

    submit = SubmitField("Gem")


class AdminEditStringForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=50)])
    submit = SubmitField("Gem")

