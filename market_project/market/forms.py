from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class RegistrationForm(FlaskForm):
    username = StringField(label='user name', validators=[DataRequired()])
    email_address = StringField(label='email address', validators=[DataRequired()])
    password1 = PasswordField(label='password', validators=[DataRequired()])
    password2 = PasswordField(label=' confirm password', validators=[DataRequired()])
    submit = SubmitField(label='create account')
