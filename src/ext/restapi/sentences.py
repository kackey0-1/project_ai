from flask import abort, jsonify, request
from flask_restful import Resource

from src.models import Sentence
from src.ext.database import db


class SentenceResource(Resource):
    def get(self):
        sentences = Sentence.query.all() or abort(204)
        return jsonify({"sentences": [sentences.to_dict() for sentence in sentences]})

    def post(self):
        """
        Creates a new sentence.

        # curl -XPOST localhost:5000/api/v1/sentence/ \
        #  -H "Authorization: Basic Y2h1Y2s6bm9ycmlz" \
        #  -H "Content-Type: application/json"
        """
        json = request.get_json(force=True)
        sentence = Sentence(input=json.get("input"))
        db.session.add(sentence)
        db.session.commit()
        return jsonify(sentence.to_dict()), 201


class SentenceItemResource(Resource):
    def get(self, id):
        sentence = Sentence.query.filter_by(id=id).first() or abort(404)
        return jsonify(sentence.to_dict())
