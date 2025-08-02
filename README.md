Author: Hossam Oraby

# CambioML Computer Use Backend

This project provides a minimal FastAPI backend for managing chat sessions and
messages. It offers REST endpoints for creating sessions, posting messages, and
retrieving history, backed by a SQLite database via SQLAlchemy. Real-time
updates are streamed to clients using Server-Sent Events (SSE) and a simple VNC
URL is exposed for connecting to the desktop used by the computer-use agent.

## Running the application

```bash
uvicorn main:app --reload
```

This starts the API server on `http://localhost:8000`. A very small HTML demo
is served from `/ui` to interact with the API and view the VNC session.

## API Endpoints

- `POST /sessions` – create a new session.
- `GET /sessions` – list all sessions.
- `POST /sessions/{session_id}/messages` – add a message to a session and
  stream it to connected clients.
- `GET /sessions/{session_id}/messages` – retrieve all messages for a session.
- `GET /sessions/{session_id}/stream` – SSE endpoint streaming new messages.
- `GET /sessions/{session_id}/vnc` – return a URL for the VNC web client.

The project also includes a simple WebSocket echo endpoint at `/ws`.

## Docker

To run the backend along with the official Anthropics computer-use demo
environment:

```bash
cd docker
docker compose up --build
```

This starts the FastAPI backend on port `8000` and a VNC/web desktop on ports
`5900` and `6080`.

