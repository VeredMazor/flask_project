from flask import Blueprint, request, render_template, flash, redirect
from werkzeug.security import generate_password_hash

from database import db
from models import User


sign_up_bp = Blueprint("sign_up_bp", __name__, static_folder="static",
                       template_folder="templates", static_url_path='/signup')

@sign_up_bp.route('/', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            if username == 'admin':
                is_admin = True
            else:
                is_admin = False
            hashed_password = generate_password_hash(password)

            user_obj = User(username=username, password=hashed_password, is_admin=is_admin)

            db.session.add(user_obj)
            db.session.commit()

            flash('You were successfully signed up', 'success')
            return redirect('/') # Redirect to the root URL
        except Exception as e:
            error = str(e)
            flash(error, 'error')

    return render_template('sign_up_page.html')