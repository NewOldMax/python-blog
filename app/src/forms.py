from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField, validators
from wtforms.validators import Required

class LoginForm(Form):
    username = TextField('Username', validators = [Required()])
    password = TextField('Password', validators = [Required()])
    remember_me = BooleanField('Remember Me', default = False)

class RegisterForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

class PostForm(Form):
    title = TextField('title', validators = [Required()])
    text = TextField('text', validators = [Required()])