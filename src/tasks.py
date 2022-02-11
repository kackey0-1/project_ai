from src import db
from .models import Sentence, Status
from src.ext import celeryapp
from transformers import T5Tokenizer, AutoModelForCausalLM

celery = celeryapp.celery
# set tokenizer and model
tokenizer = T5Tokenizer.from_pretrained("./japanese-gpt2-medium")
model = AutoModelForCausalLM.from_pretrained("./japanese-gpt2-medium")


@celery.task()
def handle_message(input_uuid):
    print("Received input id: {}".format(input_uuid))
    print(input_uuid)
    sentence = Sentence.query.filter_by(id=input_uuid).first()
    sentence.status = Status.FINISHED
    sentence.output = "FINISHED"
    input_data = tokenizer.encode(sentence.input, return_tensors="pt")
    output = model.generate(
        input_data, do_sample=True, max_length=100, num_return_sequences=8
    )
    sentence.output = output
    print(tokenizer.batch_decode(output))
    db.session.add(sentence)
    db.session.commit()
