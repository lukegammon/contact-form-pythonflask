from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField

class RegistrationForm(FlaskForm):
    email = StringField('email', [validators.Email(), validators.Length(min=6, max=30), validators.DataRequired()])
    firstname = StringField('firstname', [validators.Length(min=2, max=25), validators.DataRequired()] )
    lastname = StringField('lastname', [validators.Length(min=2, max=25), validators.DataRequired()])
    password = PasswordField('password', [validators.DataRequired()])
    #tcaccepted = BooleanField('tcaccepted', [validators.DataRequired()])
    submit = SubmitField('Submit')