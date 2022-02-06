import enum

from sqlalchemy import Sequence
from sqlalchemy_serializer import SerializerMixin
from src.ext.database import db


class Status(str, enum.Enum):
    QUEUED = "QUEUED"
    PROCESSING = "PROCESSING"
    FINISHED = "FINISHED"


class Sentence(db.Model, SerializerMixin):
    sentence_id_seq = Sequence("sentence_id_seq")
    id = db.Column(
        db.String(36),
        primary_key=True,
    )
    status = db.Column(db.Enum(Status), nullable=False, default=Status.QUEUED)
    input = db.Column(db.String(100), nullable=False)
    context = db.Column(db.Text)
