from fastapi.testclient import TestClient
import pytest
from main import app, client, settings

api = TestClient(app)
client.drop_database(settings.db_name)

@pytest.fixture
def post_game():
    game_name = 'World of Warcarft'
    game = {
        'name': game_name,
        'producer': 'Blizzard'
    }

    return api.post("/games/", json=game)

@pytest.fixture
def get_all():
    return api.get('/games/')

def test_get_all_games_api( get_all):
    assert get_all.status_code == 200
    assert get_all.json() == []

def test_insert_update_game_api(post_game):
    response = post_game
    assert response.status_code == 200
    assert 'id' in response.json().keys()

    game_id = response.json()['id']    
    new_name = "Diablo 2"
    updated_game = {
        'name': new_name,
        'producer': post_game.json()['producer']
    }
    update_response = api.put(f"/game/{game_id}", json=updated_game)
    assert update_response.status_code == 200
    
    all_games = api.get('/games/')
    assert len(all_games.json()) == 1
    
    get_game = api.get(f"/games/{game_id}")
    assert get_game.status_code == 200
    assert get_game.json()['name'] == new_name

    delete_response = api.delete(f"/game/{game_id}")
    assert delete_response.status_code == 204

