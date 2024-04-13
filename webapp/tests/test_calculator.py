import pytest
from webapp.app import app


@pytest.fixture
def client():
    """Create a test client for the app."""
    with app.test_client() as client:
        yield client


def test_hello(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, World!" in response.data


def test_calculator_add(client):
    response = client.get("/calculator?num1=5&num2=10&operation=add")
    assert response.status_code == 200
    assert b"The result of 5.0 add 10.0 is 15.0." in response.data
