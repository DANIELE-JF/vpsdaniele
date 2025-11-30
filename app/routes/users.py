from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user
from app.models.user import User

users_bp = Blueprint('users', __name__)

@users_bp.route("/")
@login_required
def list_users():
    users = User.query.all()
    return render_template("users/list.html", users=users)

@users_bp.route("/<int:user_id>")
@login_required
def user_detail(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("users/detail.html", user=user)

