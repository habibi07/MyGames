from fastapi.testclient import TestClient
import pytest
from main import app, client, settings

api = TestClient(app)

@pytest.fixture(scope='module', autouse=True)
def fixture():
    client.drop_database(settings.db_name)


def test_get_all_games_api():
    response = api.get("/games/")
    assert response.status_code == 200
    assert response.json() == []

def test_insert_update_game_api():
    game_name = 'World of Warcarft'
    game = {
        'name': game_name,
        'producer': 'Blizzard'
    }

    response = api.post("/games/", json=game)
    assert response.status_code == 200
    assert 'id' in response.json().keys()
    assert game_name == response.json()['name']

    game_id = response.json()['id']
    
    new_name = "Diablo 2"
    updated_game = dict(**updated_game, name=new_name)
    update_response = api.put(f"/game/{game_id}", json=updated_game)

