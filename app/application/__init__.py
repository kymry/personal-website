from flask import Flask
from .config import Config
from .errors.routes import bp as error_bp
from .routes import bp as routes_bp


def create_app():

	app = Flask(__name__)
	app.config.from_object(Config)

	with app.app_context():
		app.register_blueprint(error_bp)
		app.register_blueprint(routes_bp)

		return app
