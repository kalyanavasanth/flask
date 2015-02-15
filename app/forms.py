from flask.ext.wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(Form):
    Name = StringField('Name', validators=[DataRequired()])
    UserName=StringField('UserName', validators=[DataRequired()])
    Email= StringField('Email', validators=[DataRequired()])
    Password=PasswordField('Password',validators=[DataRequired()])
    ConfirmPassword=PasswordField('ConfirmPassword',validators=[DataRequired()])