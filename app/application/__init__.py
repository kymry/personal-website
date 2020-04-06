from flask import Flask
from .config import Config
from .personal.routes import bp as personal_bp
from .errors.routes import bp as error_bp
from .sentiment.routes import bp as sentiment_bp


def create_app():

	app = Flask(__name__)
	app.config.from_object(Config)

	with app.app_context():
		app.register_blueprint(personal_bp)
		app.register_blueprint(error_bp)
		app.register_blueprint(sentiment_bp)

		return app
