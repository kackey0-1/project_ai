from .base import create_celery_app

app = create_celery_app()


@app.task
def handle_message(message):
    print("Received message: {0!r}".format(message))


# from celery import bootsteps
# from kombu import Consumer, Exchange, Queue
# generate_sentence_key = "generate_sentence_queue"
# celery = create_celery_app()
# generate_sentence_queue = Queue(
#     generate_sentence_key,
#     Exchange(generate_sentence_key),
#     generate_sentence_key,
# )
#
#
# class GenerateSentenceConsumerStep(bootsteps.ConsumerStep):
#     def get_consumers(self, channel):
#         return [
#             Consumer(
#                 channel,
#                 queues=[generate_sentence_queue],
#                 callbacks=[self.handle_message],
#                 accept=["json"],
#             )
#         ]
#
#     def handle_message(self, body, message):
#         print("Received message: {0!r}".format(body))
#         message.ack()
