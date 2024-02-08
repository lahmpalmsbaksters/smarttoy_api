# app/main.py

from fastapi import FastAPI
from app.api.endpoints import user
from app.api.endpoints import healthcheck

app = FastAPI()

app.include_router(user.router)
app.include_router(healthcheck.router)
