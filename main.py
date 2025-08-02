from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api import api_router
from app.db import init_db


app = FastAPI()
init_db()
app.include_router(api_router)
app.mount("/ui", StaticFiles(directory="static", html=True), name="ui")

