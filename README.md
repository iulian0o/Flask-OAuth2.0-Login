# Flask Authentication App with Google OAuth

A simple Flask web application demonstrating user authentication with **username/password** and **Google OAuth 2.0**, using **SQLite** as the database backend.

---

## Features

- User registration and login with username and password
- Login using **Google OAuth 2.0**
- Password hashing for security
- Session management for authenticated users
- Simple dashboard for logged-in users
- Logout functionality

---

## Tech Stack

- **Backend:** Flask
- **Database:** SQLite (via SQLAlchemy)
- **Authentication:**  
  - Traditional username/password  
  - **Google OAuth 2.0**
- **Security:** Werkzeug password hashing
- **Templates:** Jinja2

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/flask-auth-app.git
cd flask-auth-app
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate

pip install -r requirements.txt

CLIENT_ID = "your_google_client_id"
CLIENT_SECRET = "your_google_client_secret"
```
python main.py

```
flask-auth-app/
│
├── app.py               # Main Flask application
├── api_key.py           # Google OAuth credentials
├── templates/           # HTML templates
│   ├── index.html       # Login/Register page
│   └── dashboard.html   # Dashboard page
├── user.db              # SQLite database (auto-created)
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```
