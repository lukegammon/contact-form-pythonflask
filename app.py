from flask import Flask, render_template, request, redirect, jsonify
from forms import RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash

# App config
app = Flask(__name__)
app.config['SECRET_KEY'] = 'StronglySecretYa'

@app.route("/")
def main():
    form = RegistrationForm()
    return render_template('create.html', title="Create Account", form=form)

@app.route("/check", methods=['GET','POST'])
def signup():
    form = RegistrationForm()
    # Validate Form
    if form.validate_on_submit():
        return form.data
    else:
        return "denied"

if __name__ == "__main__":
    app.run(debug=True)