from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Session(Base):
    """Database model representing a chat session."""

    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String(50), default="active")
    messages = relationship("Message", back_populates="session")


class Message(Base):
    """Database model representing a chat message."""

    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("sessions.id"))
    content = Column(Text)
    type = Column(String(50))  # user, assistant, system
    timestamp = Column(DateTime, default=datetime.utcnow)
    session = relationship("Session", back_populates="messages")

