from fastapi import FastAPI

from app.api import api_router
from app.db import init_db


app = FastAPI()
init_db()
app.include_router(api_router)

