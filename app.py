from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('login.html');

@app.route("/api/login")
def login():
    return"<h1>This is the login page</h1>"

if __name__ == "__main__":
    app.run()