from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required
from app.forms.loginForm import LoginForm
from app.forms.signUpForm import SignUpForm
from app.models.user import User
from app.extensions import db
from werkzeug.security import check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    errors = []
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get("next")
            return redirect(next_page or url_for("main.profile"))
        else:
            errors.append("Invalid username or password")
    else:
        print(form.errors)
    return render_template("auth/login.html", form=form, errors=errors)

@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    errors = []
    
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        
        try:
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for("main.profile"))
        except Exception as e:
            db.session.rollback()
            errors.append("An error occurred. Please try again.")
            print(e)
    
    return render_template("auth/signup.html", form=form, errors=errors)

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

