from .database import SessionLocal, engine, get_db
from .models import Base


def init_db() -> None:
    """Create database tables."""
    Base.metadata.create_all(bind=engine)

