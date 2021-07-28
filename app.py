from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug import datastructures
from forms import RegistrationForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os
load_dotenv()

# App config
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
# Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
# Initialize Database
db = SQLAlchemy(app)
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(150), nullable=False)
    agreedtc = db.Column(db.String(5), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    # Create a string
    def __repr__(self):
        return '<email %r>' % self.email


@app.route("/")
def main():
    if 'email' in session:
        firstname = session['firstname']
        return render_template('dashboard.html', title="Dashboard", firstname=firstname.capitalize())
    form = RegistrationForm()
    return render_template('signup.html', title="Create Account", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if 'email' in session:
        firstname = session['firstname']
        return render_template('dashboard.html', title="Dashboard", firstname=firstname.capitalize())
    if request.method == 'POST':
        form = LoginForm()
        if form.validate_on_submit():
            email = request.form['email']
            password = request.form['password']
            user = Users.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                session['email'] = user.email
                session['firstname'] = user.firstname
                return render_template('dashboard.html', title="Dashboard", firstname=user.firstname.capitalize())
            return render_template('failure.html', redirect_path="/login", title="Failure", error="Login")
        return render_template('failure.html', redirect_path="/login", title="Failure", error="Login")
    return render_template('login.html', title="Login", form=LoginForm())

@app.route("/logout")
def logout():
    if 'email' in session:
        session.pop('email')
        session.pop('firstname')
    return render_template('login.html', title="Login", form=LoginForm())
        

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        form = RegistrationForm()
        hashed_password = generate_password_hash(form.password.data)
        user = Users.query.filter_by(email=form.email.data).first()
        if form.validate_on_submit() and not user:
            newuser = Users(
                email = form.email.data,
                firstname = form.firstname.data,
                lastname = form.lastname.data,
                password = hashed_password,
                agreedtc = form.tcaccepted.data
                )
            db.session.add(newuser)
            db.session.commit()
            return render_template('login.html', title="Login", form=LoginForm())
        else:
            print("failed signup")
            return render_template('failure.html', error="Sign up", redirect_path="/", title="Failure")
    return render_template('signup.html', form=RegistrationForm(), title="Signup")

if __name__ == "__main__":
    app.run(debug=True)