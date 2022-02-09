# __init__.py is a special Python file that allows a directory to become
# a Python package so it can be accessed using the 'import' statement.
from dynaconf import FlaskDynaconf
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# Instantiate Flask extensions
from src.ext import celeryapp

db = SQLAlchemy()


def create_app():
    """Create a Flask application.
    """
    app = Flask(
        __name__, static_folder="../ui/dist/static", template_folder="../ui/dist"
    )
    # Instantiate Flask
    FlaskDynaconf(app)  # config managed by Dynaconf
    # Celery
    # Load common settings
    # app.config.from_object('app.settings')
    # Load environment specific settings
    # app.config.from_object('app.local_settings')
    # Load extra settings from extra_config_settings param
    # Setup Flask-SQLAlchemy
    create_worker_app(app)
    app.config.load_extensions("EXTENSIONS")  # Load extensions from settings.toml
    return app


def create_worker_app(app=None):
    """Minimal App without routes for celery worker."""
    if app is None:
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../development.db'
    db.init_app(app)
    celery = celeryapp.create_celery_app(app)
    celeryapp.celery = celery
    return app
