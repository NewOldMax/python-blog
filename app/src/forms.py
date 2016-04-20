from wtforms import Form, BooleanField, TextField, PasswordField

class LoginForm(Form):
    openid = TextField('openid')
    remember_me = BooleanField('remember_me')