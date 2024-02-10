import os
from flask import Flask, send_from_directory
from flask_migrate import Migrate
from config import Config
from database import db
from flask_login import LoginManager
from models import User

from index.index import index_bp
from login.login_page import login_bp
from signup.sign_up import sign_up_bp
from home.home_page import home_page_bp
from admin.admin_dashboard import admin_dashboard_bp
from gameinfo.game_info import game_info_bp



app = Flask(__name__)
app.config.from_object(Config)

# SQLAlchemy instance creation
db.init_app(app)
migrate = Migrate(app, db)

# Initialize the LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

# Define the user loader function
@login_manager.user_loader
def load_user(user_id):
    # Return the user object corresponding to the user ID
    return User.query.get(int(user_id))

# Initialize Flask-Login with the app
login_manager.init_app(app)

# Define the login view for unauthorized users
login_manager.login_view = 'login_bp.login'

app.register_blueprint(index_bp, url_prefix="/")
app.register_blueprint(login_bp, url_prefix="/login")
app.register_blueprint(sign_up_bp, url_prefix="/signup")
app.register_blueprint(home_page_bp, url_prefix="/home")
app.register_blueprint(admin_dashboard_bp, url_prefix="/admin_dashboard")
app.register_blueprint(game_info_bp, url_prefix="/game_info")




@app.route('/uploads/<filename>', methods=['GET', 'POST'])
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True) #make directory to upload images.
    app.run(debug=True)