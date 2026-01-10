🔐 Flask Authentication System

A simple Flask-based authentication system featuring user registration, login, logout, and session-based access control.
Passwords are securely hashed, and user data is stored using SQLite + SQLAlchemy.

🚀 Features

User Registration

User Login & Logout

Password Hashing (Werkzeug)

Session-based Authentication

Protected Dashboard Route

SQLite Database (via SQLAlchemy)

Clean UI with HTML + SCSS/CSS

🛠️ Tech Stack

Python

Flask

Flask-SQLAlchemy

Werkzeug Security

SQLite

HTML / CSS / SCSS

JavaScript (Form handling)

📂 Project Structure
Flask-Login-System/
│
├── main.py
├── user.db
│
├── templates/
│   ├── base.html
│   ├── index.html
│   └── dashboard.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/flask-login-system.git
cd flask-login-system

2️⃣ Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install flask flask-sqlalchemy werkzeug

▶️ Running the Application
python main.py


The app will run at:

http://127.0.0.1:5000/

🔑 How It Works
📝 Registration

Users can register with a unique username and password

Passwords are hashed using generate_password_hash

User data is saved in an SQLite database

🔓 Login

Credentials are validated against the database

Passwords are verified using check_password_hash

Session is created on successful login

📊 Dashboard

Accessible only when logged in

Displays a welcome message with the username

🚪 Logout

Clears the session

Redirects back to the home page

🔒 Security Notes

Passwords are never stored in plain text

Session-based authentication

Secret key required for session management (replace in production)
