from unittest.mock import patch
from User import User


def test_index():
    with patch("app.session", dict()) as session:
        client = app.test_client()
        response = client.post("/", data={
            "username": "test"
        })
        assert session.get("username") == "test"
        assert response.data == b"Username saved in session"
