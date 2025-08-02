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
- `GET /sessions/{session_id}/vnc` – obtain a VNC URL for the session.

The project also includes a simple WebSocket echo endpoint at `/ws`.

## Using with Anthropic Quickstarts

This backend can be paired with the [Anthropic Quickstarts Computer Use Demo](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo).
For convenience a `computer-use-demo` directory is included in this repository; populate it with the quickstart frontend by copying the files from the upstream project.
Run this API server and then start the quickstart front end. The front end will
communicate with the endpoints above and use `/sessions/{id}/vnc` to retrieve
the VNC connection URL.

