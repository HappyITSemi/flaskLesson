# pip install Flask-WTF
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class UserForm(FlaskForm):
    id = IntegerField()  # hidden type
    name = StringField()
    submit = SubmitField()




