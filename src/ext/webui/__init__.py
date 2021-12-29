from flask import Blueprint

from .views import index

bp = Blueprint(
    "webui",
    __name__,
)
bp.add_url_rule("/", view_func=index)


def init_app(app):
    app.register_blueprint(bp)
