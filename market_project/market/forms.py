from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField(label='user name', validators=[DataRequired(), Length(min=2, max=20)])
    email_address = StringField(label='email address', validators=[DataRequired(), Email()])
    password1 = PasswordField(label='password', validators=[DataRequired(),Length(min=6)])
    password2 = PasswordField(label=' confirm password', validators=[DataRequired(), EqualTo('password1')])
    submit = SubmitField(label='create account')
