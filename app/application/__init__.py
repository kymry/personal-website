from flask import Flask
from app.application.config import Config
from app.application.personal.routes import bp as personal_bp
from app.application.errors.routes import bp as error_bp
from app.application.sentiment.routes import bp as sentiment_bp
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def create_app():

	app = Flask(__name__)
	app.config.from_object(Config)

	db.init_app(app)
	migrate.init_app(app, db)

	with app.app_context():
		app.register_blueprint(personal_bp)
		app.register_blueprint(error_bp)
		app.register_blueprint(sentiment_bp)

		return app
