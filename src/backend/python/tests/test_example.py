import requests


def test_info_endpoint():
    response = requests.get("http://127.0.0.1:8080/info")
    assert response.status_code == 200
    assert response.content == "Hello from backend"
