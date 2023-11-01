"""test.conftest
All the fixtures for testing.
"""
import pytest

from fastapi.testclient import TestClient

from src.main import app


@pytest.fixture
def app_client():
    client = TestClient(app)
    return client
