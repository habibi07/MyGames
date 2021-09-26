import use_cases
import asyncio
import pytest
from main import get_collection, client, settings
from models import GameIn, GameOut

collection = get_collection()

@pytest.fixture(scope='module', autouse=True)
def setup_fixture():
    client.drop_database(settings.db_name)

@pytest.fixture
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.mark.asyncio
async def test_get_all_games_use_case():
    games = await use_cases.get_all_games(collection)
    assert len(games) == 0
    assert type(games) is list

    new_game = GameIn(name='World of Warcraft', producer='blizzard')
    added_game = await use_cases.save_game(collection, new_game)
    assert type(added_game) is GameOut

    new_game_name = 'Diablo 2'
    changed_game = GameIn(name=new_game_name, producer='Blizzard')
    changed_game = await use_cases.save_game(collection, changed_game, added_game.id)
    assert changed_game.name == new_game_name
