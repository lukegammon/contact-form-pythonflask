from flask import Flask, render_template, request, redirect, jsonify
from wtforms import Form, BooleanField, StringField, PasswordField, validators

# App config
DEBUG=True
app = Flask(__name__)

class RegistrationForm(Form):
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    firstname = StringField('Firstname ', [validators.Length(min=2, max=25)])
    lastname = StringField('Lastname', [validators.Length(min=2, max=25)])
    password = PasswordField('Password', [validators.DataRequired()])
    tcaccepted = BooleanField('I accept the TOS', [validators.DataRequired()])

@app.route("/")
def main():
    return render_template('login.html')

@app.route("/check", methods=['GET','POST'])
def signup():
    form = RegistrationForm(request.form)
    if request.method == "POST":
        email = form.email
        firstname = form.firstname
        lastname = form.lastname
        password = form.password
        tcaccepted = form.tcaccepted
        if tcaccepted == 'on':
            tcaccepted = True
        else:
            tcaccepted = False
        return jsonify(
            email=email,
            firstname=firstname,
            lastname=lastname,
            password=password,
            tcaccepted=tcaccepted
        )
    return render_template("login.html")
"""     message=''
    if request.method == 'POST':
        username = request.form.get('username')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        tcagreed = request.form.get('checkbox')
        response_body = {
            "username": username,
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "tcagreed" : tcagreed
        }
        return response_body """

if __name__ == "__main__":
    app.run()