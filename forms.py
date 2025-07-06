from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField,SubmitField
from wtforms.validators import DataRequired,Email,Length

class ContactForm(FlaskForm):
    name = StringField('Enter name',validators=[DataRequired()])
    email = EmailField('Enter your mail',validators=[DataRequired(),Email()])
    message = TextAreaField('Message',validators=[DataRequired(),Length(min=10, message="Message must be at least 10 characters long.")])
    submit = SubmitField('Send message')
    