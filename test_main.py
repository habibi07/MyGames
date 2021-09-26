from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_all_games_api():
    response = client.get("/games/")
    assert response.status_code == 200
    assert response.json() == []
