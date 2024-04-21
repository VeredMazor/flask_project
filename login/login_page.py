from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask_login import login_user
from werkzeug.security import check_password_hash
from models import User


login_bp = Blueprint("login_bp", __name__, static_folder="static",
                         template_folder="templates", static_url_path='/login')



@login_bp.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        # Validate the username
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            # If the username and password match, set a cookie and redirect to home page
            login_user(user)  # Login the user
            #resp = make_response(redirect(url_for('home_page_bp.home_page')))
            #resp.set_cookie('username', username)
            flash('You were successfully logged in')
            return redirect(url_for('home_page_bp.home_page'))
        else:
            # If validation fails, display an error message
            error = "Invalid username or password. Please try again."
            return render_template('login_page.html', error=error)

    # Render the login page
    return render_template('login_page.html')