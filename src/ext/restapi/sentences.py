from flask import abort, jsonify, request
from flask_restful import Resource
from src.models import Sentence
from src import db
from uuid import uuid4
from src import tasks


class SentenceResource(Resource):
    def get(self):
        sentences = Sentence.query.all() or abort(204)
        return jsonify({"sentences": [sentence.to_dict() for sentence in sentences]})

    def post(self):
        """
        Creates a new sentence.

        # curl -XPOST localhost:5000/api/v1/sentence/ \
        #  -H "Authorization: Basic Y2h1Y2s6bm9ycmlz" \
        #  -H "Content-Type: application/json"
        """
        json = request.get_json(force=True)
        input_uiid = str(uuid4())
        sentence = Sentence(id=input_uiid, input=json.get("input"))
        db.session.add(sentence)
        db.session.commit()
        tasks.handle_message.delay(input_uiid)
        return jsonify(sentence.to_dict())


class SentenceItemResource(Resource):
    def get(self, id):
        sentence = Sentence.query.filter_by(id=id).first() or abort(404)
        return jsonify(sentence.to_dict())

