Author: Hossam Oraby

# CambioML Computer Use Backend

This project provides a minimal FastAPI backend for managing chat sessions and
messages. It offers REST endpoints for creating sessions, posting messages, and
retrieving history, backed by a SQLite database via SQLAlchemy.

## Running the application

```bash
uvicorn main:app --reload
```

This will start the API server on `http://localhost:8000`.

## API Endpoints

- `POST /sessions` – create a new session.
- `GET /sessions` – list all sessions.
- `POST /sessions/{session_id}/messages` – add a message to a session.
- `GET /sessions/{session_id}/messages` – retrieve all messages for a session.

The project also includes a simple WebSocket echo endpoint at `/ws`.

