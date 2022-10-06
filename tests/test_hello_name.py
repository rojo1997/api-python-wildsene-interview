"""Test hello name endpoint"""
import sys
from fastapi.testclient import TestClient

sys.path.append("./app")

from app.main import app


def test_0():
    """Test 0: Hello world.

    Giving a name as parameter, should return 'Hello {name} !'
    """
    client = TestClient(app)
    response = client.get(url="/hello/Wildsense")
    assert response.ok, str(response.json())
    assert response.content.decode("utf-8") == "Hello Wildsense !"


def test_1():
    """Test 1: Hello world.

    Giving a name as parameter, should return 'Hello {name} !'
    """
    client = TestClient(app)
    params = {"name": 123}
    response = client.get(url="/hello/123", params=params)
    assert response.ok, str(response.json())
    assert response.content.decode("utf-8") == "Hello 123 !"
