from flask import Flask
from .extensions import db, migrate
from .routes import main_bp
from .config import DevelopmentConfig
import os
from dotenv import load_dotenv

load_dotenv()


def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig())
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(main_bp)
    return app