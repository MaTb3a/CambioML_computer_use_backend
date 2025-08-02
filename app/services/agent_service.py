from sqlalchemy.orm import Session
from app.db import models


def create_session(db: Session) -> models.Session:
    """Create and persist a new session."""
    session = models.Session()
    db.add(session)
    db.commit()
    db.refresh(session)
    return session


def add_message(db: Session, session_id: int, content: str, type_: str) -> models.Message:
    """Persist a new message for the given session."""
    session = db.query(models.Session).filter(models.Session.id == session_id).first()
    if session is None:
        raise ValueError("Session not found")
    message = models.Message(session_id=session_id, content=content, type=type_)
    db.add(message)
    db.commit()
    db.refresh(message)
    return message

