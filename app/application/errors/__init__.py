from flask import Blueprint

bp = Blueprint('errors', __name__)

from app.application.errors import routes