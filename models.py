from database import db
from flask_login import UserMixin


class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), unique=True, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def is_active(self):
        # Return True if the user is considered active, False otherwise
        return True


class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(252), nullable=False)
    platform = db.Column(db.String(50), nullable=False)
    release_date = db.Column(db.String(50), nullable=True)
    publisher = db.Column(db.String(50), nullable=True)
    description = db.Column(db.String(252), nullable=True)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'), nullable=False)

    # Define relationships with User and Games
    user = db.relationship('User', backref=db.backref('comments', lazy=True))
    game = db.relationship('Games', backref=db.backref('comments', lazy=True))

