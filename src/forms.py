from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DecimalField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from src.models import User
from flask_login import current_user

class RegistrationForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired(), Length(min=1, max=50)])
    last_name = StringField('Last name', validators=[DataRequired(), Length(min=1, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:  # i.e. if user != None
            raise ValidationError('Email already in use. Please choose a different email.')

# Template for custom validation methods:
#    def validate_field(self, field):
#        if conditional:
#            raise ValidationError('Message')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired(), Length(min=1, max=50)])
    last_name = StringField('Last name', validators=[DataRequired(), Length(min=1, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    img = FileField('Update profile picture', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Update')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:  # i.e. if user <> None
                raise ValidationError('Email already in use. Please choose a different email.')

class RequestForm(FlaskForm):
    requester_name = StringField('Your name', validators=[DataRequired()])
    text = StringField('Description', validators=[DataRequired()])
    amount = DecimalField('Request amount', validators=[DataRequired()])
