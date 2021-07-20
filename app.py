from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# App config
app = Flask(__name__)
app.config['SECRET_KEY'] = 'StronglySecretYa'
# Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
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
        return '<Name %r>' % self.name


@app.route("/")
def main():
    form = RegistrationForm()
    return render_template('create.html', title="Create Account", form=form)

@app.route("/check", methods=['POST'])
def signup():
    form = RegistrationForm()
    hashed_value = generate_password_hash(form.password.data)
    passwordcheck = check_password_hash(hashed_value, form.password.data)
    print(passwordcheck)
    # Validate Form
    if form.validate_on_submit():
        # redirect to loggedin page
        return form.data
    else:
        # redirect to signup page or handle errors
        return "denied"

if __name__ == "__main__":
    app.run(debug=True)