"""src.routers.healthcheck
This module contains the url for healthcheck.
"""
from os import environ
from fastapi import APIRouter

healthcheck_router = APIRouter()


@healthcheck_router.get("/healthcheck")
async def healthcheck():
    return {
        "API Status": "working",
        "API Version": f"{environ.get('API_VERSION')}"
    }
