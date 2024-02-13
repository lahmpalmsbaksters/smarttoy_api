# app/main.py

from fastapi import FastAPI
from app.api.endpoints import user
from app.api.endpoints import healthcheck
from app.api.endpoints import handgesture

app = FastAPI()

app.include_router(user.router)
app.include_router(healthcheck.router)
app.include_router(handgesture.router)
