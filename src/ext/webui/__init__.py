from flask import Blueprint

from .views import index, redirect_to_index

bp = Blueprint(
    "webui",
    __name__,
)
bp.add_url_rule("/", view_func=index)
bp.add_url_rule("/<string:text>", view_func=redirect_to_index)


def init_app(app):
    """
    :param app:
    :return:
    """
    app.register_blueprint(bp)
