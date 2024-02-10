from flask import Blueprint, request, render_template, flash, redirect, url_for
from models import Games, Comment, User
from flask_login import current_user

from database import db
from sqlalchemy.orm import joinedload

game_info_bp = Blueprint("game_info_bp", __name__, static_folder="static",
                         template_folder="templates", static_url_path='/game_info')


@game_info_bp.route("/<game_title>")
def game_info(game_title):
    game = Games.query.filter_by(title=game_title).first()
    comment = Comment.query.all()

    current_username = current_user
    user_current = User.query.filter_by(username=current_username.username).first() if current_username else None

    if game:
        return render_template('game_info_page.html', game=game, comments=comment, current_user=user_current)
    else:
        flash(f'Game with title {game_title} not found', 'error')
        return redirect(url_for('home_page'))


@game_info_bp.route('/add_comment/<game_title>', methods=['POST'])
def add_comment(game_title):
    game = Games.query.filter_by(title=game_title).first()

    if game:
        if not current_user.is_authenticated:
            flash('You need to log in to add a comment.', 'error')
            return redirect(url_for('login'))

        comment_text = request.form.get('comment_text')

        new_comment = Comment(text=comment_text, user=current_user, game=game)

        db.session.add(new_comment)
        db.session.commit()

        flash('Comment added successfully!', 'success')

    return redirect(url_for('game_info_bp.game_info', game_title=game_title))

@game_info_bp.route('/delete_comment/<int:comment_id>', methods=['GET', 'POST'])
def delete_comment(comment_id):
    # Retrieve the comment with the 'game' relationship preloaded
    comment = (
        db.session.query(Comment)
        .options(joinedload(Comment.game))
        .get(comment_id)
    )

    if comment:
        if not current_user.is_authenticated or comment.user_id != current_user.id:
            flash('You are not authorized to delete this comment.', 'error')
        else:
            db.session.delete(comment)
            db.session.commit()
            flash('Comment deleted successfully!', 'success')
    else:
        flash('Comment not found.', 'error')

    # Redirect to the appropriate game_info page
    game_title = comment.game.title if comment and comment.game else None
    return redirect(url_for('game_info_bp.game_info', game_title=game_title))
