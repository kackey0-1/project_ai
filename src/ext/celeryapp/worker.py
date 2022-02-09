"""
Run using the command:

python celery -A app.celeryapp.celery_worker.celery worker --concurrency=2 -E -l info
"""
from src.ext import celeryapp
from src import create_worker_app

app = create_worker_app()
celery = celeryapp.create_celery_app(app)
celeryapp.celery = celery
