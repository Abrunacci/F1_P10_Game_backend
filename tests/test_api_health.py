"""tests.test_api_health
This module tests the API health.
"""
from fastapi import APIRouter


def test_api_health(app_client):
    """Test API health"""
    response = app_client.get('/healthcheck')
    assert response.status_code == 200
    assert response.json() == {
        "API Status": "working",
        "API Version": "1"
    }

