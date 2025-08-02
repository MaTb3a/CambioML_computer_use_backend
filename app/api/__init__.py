from fastapi import APIRouter

from .routes import router as routes_router
from .websockets import router as websockets_router

# Combine HTTP and WebSocket routes into a single router that the main
# FastAPI application can include.
api_router = APIRouter()
api_router.include_router(routes_router)
api_router.include_router(websockets_router)

__all__ = ["api_router", "APIRouter"]

