from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,TextAreaField
from wtforms.validators import InputRequired,Email,EqualTo
from ..models import User


class ReviewForm(FlaskForm):

    username = StringField('Name',validators=[InputRequired()])
    email = TextAreaField('Email', validators=[InputRequired()])
    password = PasswordField('New Password', [InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Repeat Password')
    submit = SubmitField('Submit')

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[InputRequired(),Email()])
    username = StringField('Enter your username',validators = [InputRequired()])
    password = PasswordField('Password',validators = [InputRequired(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [InputRequired()])
    submit = SubmitField('Sign Up')    