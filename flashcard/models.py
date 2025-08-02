import uuid

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.orm import relationship

from db.db import Base

#TODO: rename flashcard to flashcards and use schemas
class FlashcardTopic(Base):
    __schema__ = "flashcard"
    __tablename__ = "topic"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)


class Flashcard(Base):
    __schema__ = "flashcard"
    __tablename__ = "flashcard"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    question = Column(String)
    answer = Column(String)
    topic_id = Column(UUID(as_uuid=True), ForeignKey("topic.id"))

    topic = relationship("FlashcardTopic", backref="flashcards")
    