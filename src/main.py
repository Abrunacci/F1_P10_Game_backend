"""src.main
This is the main module. FastAPI application get created here.
"""

from os import environ

from fastapi import FastAPI

from src.routers.healthcheck import healthcheck_router


ALL_ROUTERS = [
    healthcheck_router
]


app = FastAPI(
    description="F1 guess the P10 and first DNF game.",
    prefix=f"api/{environ.get('API_VERSION')}",
)

for route in ALL_ROUTERS:
    app.include_router(route)
