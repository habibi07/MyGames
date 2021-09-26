import motor.motor_asyncio
import use_cases

from fastapi import FastAPI
from typing import List
from models import GameIn, GameOut
from config import Settings

settings = Settings()
client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongo_dsn)
app = FastAPI()


def get_collection():
    return client[settings.db_name][settings.col]

collection = get_collection()

@app.get('/games/{game_id}', response_model=GameOut)
async def get_game(game_id: str):
    """
    Zwraca informacje o grze
    """
    return await use_cases.get_game_by_id(collection, game_id)

@app.get('/games/', response_model=List[GameOut])
async def get_games():
    """
    Zwraca wszystkie gry
    """
    return await use_cases.get_all_games(collection)

@app.post('/games/', response_model=GameOut)
async def post_game(game: GameIn):
    """
    Pozwala dodać grę
    """
    return await use_cases.save_game(collection, game)

@app.delete('/game/{game_id}', status_code=204)
async def delete_game(game_id: str):
    """
    Usuwa grę
    """
    return await use_cases.delete_game(collection, game_id)

@app.put('/game/{game_id}', response_model=GameOut)
async def put_game(game: GameIn, game_id: str):
    """
    Pozwala zmodyfikować grę
    """
    return await use_cases.save_game(collection, game, game_id)

