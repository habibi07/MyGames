import use_cases
import asyncio
import pytest
from main import get_collection

collection = get_collection()

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
    assert 5==1
