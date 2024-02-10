import secrets

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    SECRET_KEY = secrets.token_hex(16)

    # Define the upload folder
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}