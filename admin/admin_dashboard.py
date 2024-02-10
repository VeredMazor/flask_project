from flask import Blueprint, request, render_template, current_app
from models import Games
from database import db
import os


admin_dashboard_bp = Blueprint("admin_dashboard_bp", __name__, static_folder="static",
                         template_folder="templates", static_url_path='/admin_dashboard')




@admin_dashboard_bp.route('/', methods=['GET', 'POST'])
def admin_dashboard():
    if request.method == 'POST':
        print(request.form['title'])
        print(request.form['platform'])
        print(request.form['release_date'])
        print(request.form['description'])
        title = request.form['title']
        image_name = request.files['img'].filename
        platform = request.form['platform']
        release_date = request.form['release_date']
        publisher = request.form['publisher']
        description = request.form['description']
        game_obj = Games(title=title, image=image_name, platform=platform, release_date=release_date, publisher=publisher, description=description)
        print(game_obj)
        db.session.add(game_obj)
        db.session.commit()


        file = request.files['img']
        print(file)
        # Save the file to the upload folder
        if file:
            upload_folder = current_app.config['UPLOAD_FOLDER']
            filename = os.path.join(upload_folder, file.filename)
            file.save(filename)
            return f"File {file.filename} uploaded successfully"
    return render_template('admin_dashboard_page.html')
        # Check if the post request has the file part
