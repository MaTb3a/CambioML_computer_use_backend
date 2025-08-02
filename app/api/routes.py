from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sse_starlette.sse import EventSourceResponse
from sqlalchemy.orm import Session

from app.db import models
from app.db.database import get_db
from app.schemas.message import Message, MessageCreate
from app.schemas.session import Session as SessionSchema
from app.services.vnc_service import get_vnc_url
from app.utils.stream_manager import stream_manager

router = APIRouter()


@router.post("/sessions", response_model=SessionSchema)
def create_session(db: Session = Depends(get_db)):
    session = models.Session()
    db.add(session)
    db.commit()
    db.refresh(session)
    return session


@router.get("/sessions", response_model=List[SessionSchema])
def list_sessions(db: Session = Depends(get_db)):
    return db.query(models.Session).all()


@router.post("/sessions/{session_id}/messages", response_model=Message)
async def create_message(
    session_id: int, message: MessageCreate, db: Session = Depends(get_db)
):
    session = db.query(models.Session).filter(models.Session.id == session_id).first()
    if session is None:
        raise HTTPException(status_code=404, detail="Session not found")
    db_message = models.Message(
        session_id=session_id, content=message.content, type=message.type
    )
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    await stream_manager.get_queue(session_id).put(db_message.content)
    return db_message


@router.get("/sessions/{session_id}/messages", response_model=List[Message])
def get_messages(session_id: int, db: Session = Depends(get_db)):
    session = db.query(models.Session).filter(models.Session.id == session_id).first()
    if session is None:
        raise HTTPException(status_code=404, detail="Session not found")
    return session.messages


@router.get("/sessions/{session_id}/stream")
async def stream_messages(session_id: int):
    queue = stream_manager.get_queue(session_id)

    async def event_generator():
        while True:
            data = await queue.get()
            yield {"data": data}

    return EventSourceResponse(event_generator())


@router.get("/sessions/{session_id}/vnc")
def vnc_url(session_id: int):
    return {"url": get_vnc_url(session_id)}

