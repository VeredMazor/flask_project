from flask import Blueprint, render_template



index_bp = Blueprint("index_bp", __name__, static_folder="static",
                         template_folder="templates", static_url_path='/')




@index_bp.route('/',methods=['GET', 'POST'])
def index():
    return render_template("index.html")
