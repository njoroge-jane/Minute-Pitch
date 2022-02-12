from unicodedata import category
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import InputRequired

class PitchForm(FlaskForm):

    title = StringField('Pitch Title',validators=[InputRequired()])
    category = SelectField('Which category?',validators=[InputRequired()])
    review = TextAreaField('Write your pitch', validators=[InputRequired()])
    submit = SubmitField('Post')