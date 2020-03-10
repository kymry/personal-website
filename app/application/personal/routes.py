from flask import Blueprint, render_template


bp = Blueprint('home_routes', __name__, url_prefix='/')


@bp.route('/', methods=['GET'])
def home():
    return render_template('home.html')
