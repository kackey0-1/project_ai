from celery import Celery
from dynaconf import FlaskDynaconf
from flask import Flask


def create_app(**config):
    app = Flask(
        __name__, static_folder="../ui/dist/static", template_folder="../ui/dist"
    )
    FlaskDynaconf(app)  # config managed by Dynaconf
    app.config.load_extensions("EXTENSIONS")  # Load extensions from settings.toml
    app.config.update(config)  # Override with passed config
    return app


def create_celery_app():
    """
    https://docs.celeryproject.org/en/master/userguide/extending.html
    :param app:
    :return:
    """
    celery = Celery(
        # app.name,
        # backend=app.config["CELERY_RESULT_BACKEND"],
        # broker=app.config["CELERY_BROKER_URL"],
        backend="redis://localhost:6379",
        broker="redis://localhost:6379",
    )
    # celery.conf.update(app.config)
    return celery


def create_app_wsgi():
    # workaround for Flask issue
    # that doesn't allow **config
    # to be passed to create_app
    # https://github.com/pallets/flask/issues/4170
    app = create_app()
    return app
