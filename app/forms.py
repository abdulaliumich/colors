from wtforms import Form, BooleanField, TextField, PasswordField, validators, ValidationError
from models import User, UserColors

def is_username_taken(form, field):
    if User.query.filter_by(username=field.data).count():
    	message="Username already taken"
    	raise ValidationError(message)

class NewUserForm(Form):
    username = TextField('Username', [validators.Required(),
    	                              validators.Length(min=3, max=50),
    	                              validators.Regexp("^[a-zA-Z0-9_]{3,}$", flags=0, message="Invalid input"),
    	                              is_username_taken])
    email = TextField('Email Address', [validators.Required(),
    	                                validators.Length(min=6, max=35),
    	                                validators.Email(message='Invalid e-mail address')])
    password = PasswordField('Password', [
        validators.Required(),
        validators.Length(min=6,max=35),
        validators.Regexp("^(?=.*[a-zA-Z])(?=.*[0-9])(?!.*[^a-zA-Z0-9_]).{5,15}$", flags=0, message="Invalid input"),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Please type in your password again')
    color = TextField('Type in your color of choice')
