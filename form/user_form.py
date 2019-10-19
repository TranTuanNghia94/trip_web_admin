from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
import datetime
from werkzeug.security import generate_password_hash


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0)])
    first_name = StringField('First Name', validators=[DataRequired(), Regexp('^[A-Za-z ]*$', 0)])
    last_name = StringField('Last Name', validators=[DataRequired(), Regexp('^[A-Za-z ]*$', 0)])
    password = PasswordField('Password', validators=[DataRequired(), Regexp('^[A-Za-z0-9_.]*$', 0,
                                                                           message='Your password invalid')])
    role = SelectField('Role', choices=[('admin', 'admin'), ('staff', 'staff')], validators=[DataRequired()])
    active = BooleanField('Active')
    submit = SubmitField('Register')


    def convert_to_json(self):
        password = generate_password_hash(self.password.data)
        date_create = str(datetime.datetime.now().date())
        return {
            'username': self.username.data,
            'password': password,
            'first_name': self.first_name.data,
            'last_name': self.last_name.data,
            'date_create': date_create,
            'role': self.role.data,
            'active': self.active.data
        }


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 20, message='Username invalid')])
    password = PasswordField('Password', validators=[DataRequired(), Regexp('^[A-Za-z0-9_.]*$', 0)])
    submit = SubmitField('Login')

    def convert_to_json(self):
        return {
            self.username.data,
            self.password.data
        }

