from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def home():
    if "username" in session:
        return redirect(url_for('dashboard.html'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)