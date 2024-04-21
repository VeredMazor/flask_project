from flask import Blueprint, render_template, redirect
from flask_login import current_user
from flask_login import login_user, logout_user
from models import Games

home_page_bp = Blueprint("home_page_bp", __name__, static_folder="static",
                         template_folder="templates", static_url_path='/home_page')


@home_page_bp.route("/")
def home_page():
    games = Games.query.all()
    return render_template('home_page.html', games=games, is_admin=current_user.is_admin)


@home_page_bp.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect('/')

@home_page_bp.route('/about', methods=['GET'])
def about():
    return render_template('about_page.html',is_admin=current_user.is_admin)


@home_page_bp.route('/faqs', methods=['GET'])
def faqs():
    return render_template('faqs_page.html',is_admin=current_user.is_admin)
