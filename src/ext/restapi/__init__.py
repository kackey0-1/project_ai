from flask import Blueprint
from flask_restful import Api

from .resources import ImageAiResource
from .sentences import SentenceResource, SentenceItemResource

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    api.add_resource(ImageAiResource, "/upload/")
    api.add_resource(SentenceResource, "/sentence/")
    api.add_resource(SentenceItemResource, "/sentence/<int:id>")
    app.register_blueprint(bp)
