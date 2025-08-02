from fastapi import APIRouter, WebSocket

router = APIRouter()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """Echo received messages back to the client.

    This is a minimal placeholder implementation to demonstrate WebSocket
    functionality during testing."""
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(data)
    except Exception:
        await websocket.close()

