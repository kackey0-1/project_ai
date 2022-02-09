from src import db
from .models import Sentence, Status
from src.ext import celeryapp

celery = celeryapp.celery


@celery.task()
def handle_message(input_uuid):
    print("Received input id: {}".format(input_uuid))
    print(input_uuid)
    sentence = Sentence.query.filter_by(id=input_uuid).first()
    sentence.status = Status.FINISHED
    sentence.output = "FINISHED"
    db.session.add(sentence)
    db.session.commit()
    # handle_message.delay(input_uuid)
    # input_data = tokenizer.encode(sentence.input, return_tensors="pt")
    # output = model.generate(
    #     input_data, do_sample=True, max_length=100, num_return_sequences=8
    # )
    # sentence.output = input_uuid
    # print(tokenizer.batch_decode(output))
