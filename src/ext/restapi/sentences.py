from flask import abort, jsonify, request
from flask_restful import Resource
from src.models import Sentence
from src.ext.database import db
from src.consumer import handle_message
from uuid import uuid4

# from kombu import Exchange, Queue
# generate_sentence_key = "generate_sentence_queue"
# generate_sentence_queue = Queue(
#     generate_sentence_key,
#     Exchange(generate_sentence_key),
#     generate_sentence_key,
# )


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
        sentence = Sentence(id=str(uuid4()), input=json.get("input"))
        db.session.add(sentence)
        handle_message.delay("world!")
        db.session.commit()
        return jsonify(sentence.to_dict())


class SentenceItemResource(Resource):
    def get(self, id):
        sentence = Sentence.query.filter_by(id=id).first() or abort(404)
        return jsonify(sentence.to_dict())


# def pubilish_a_message(who, producer=None):
#     app = create_celery_app()
#     with app.producer_or_acquire(producer) as producer:
#         producer.publish(
#             {"hello": who},
#             serializer="json",
#             exchange=generate_sentence_queue.exchange,
#             routing_key=generate_sentence_key,
#             declare=[generate_sentence_queue],
#             retry=True,
#         )
