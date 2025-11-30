# Flask Application

A Flask application with authentication system.

## Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── extensions.py
│   ├── forms/
│   │   ├── __init__.py
│   │   ├── loginForm.py
│   │   ├── resetUserForm.py
│   │   └── signUpForm.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── routes/
│   │   ├── auth_bp.py
│   │   ├── main_bp.py
│   │   └── users.py
│   └── templates/
│       ├── base.html
│       └── auth/
│           ├── index.html
│           ├── login.html
│           ├── profile.html
│           └── signup.html
├── instance/
├── migrations/
├── configs.py
├── extensions.py
├── main.py
├── pyproject.toml
├── .env
└── README.md
```

## Setup

1. Create a virtual environment:
```bash
python -m venv .venv
```

2. Activate the virtual environment:
- Windows: `.venv\Scripts\activate`
- Linux/Mac: `source .venv/bin/activate`

3. Install dependencies:
```bash
pip install -r requirements.txt
```

Or if using uv:
```bash
uv pip install -e .
```

4. Initialize the database:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

5. Run the application:
```bash
python main.py
```

Or:
```bash
flask run
```

## Features

- User authentication (login, signup, logout)
- User profile page
- Password hashing with Werkzeug
- Flask-Login for session management
- Database migrations with Flask-Migrate
- Form validation with Flask-WTF

# vpssdaniele
