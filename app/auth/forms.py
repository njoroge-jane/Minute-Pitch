from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,TextAreaField
from wtforms.validators import InputRequired,DataRequired,Email,EqualTo
from ..models import User


class ReviewForm(FlaskForm):

    username = StringField('Name',validators=[InputRequired()])
    email = TextAreaField('Email', validators=[InputRequired()])
    password = PasswordField('New Password', [InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Repeat Password')
    submit = SubmitField('Submit')