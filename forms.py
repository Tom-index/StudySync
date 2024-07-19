from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

#==================================================
# フォーム
#==================================================
class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=255)])
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6,max=255)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    faculty = StringField('Faculty', validators=[DataRequired(), Length(max=20)])
    year = IntegerField('Year', validators=[DataRequired()])
    submit = SubmitField('Sign Up')