from typing import List
from fastapi import HTTPException

from models import GameIn, GameOut

async def get_game_by_id(collection, game_id: str) -> GameOut:
    """
    Zwraca pojedyńczą grę na podstawie id lub wyrzuca błað gdy 
    gry nie znaleziono
    """
    document = await collection.find_one({'_id': ObjectId(game_id)})
    if not document:
        raise HTTPException(status_code=404, detail="Game not found")
    return GameOut.from_mongo_result(document)

async def insert_game(collection, game: GameIn) -> GameOut:
    """
    Dodaje grę do kolekcji
    """
    gameOut = await collection.insert_one(game.dict())
    newGame = await collection.find_one({'_id': gameOut.inserted_id})
    return GameOut.from_mongo_result(newGame)

async def update_game(collection, game: GameIn, game_id: str) -> GameOut:
    """
    Aktualizuje istniejącą grę
    """
    pass

async def save_game(collection, game: GameIn, game_id: str = None) -> GameOut:
    """
    Zapis lub aktualizacja gry
    """
    if game_id:
        return await update_game(collection, game, game_id)
    else:
        return await insert_game(collection, game) 

async def delete_game(collection, game_id: str) -> bool:
    """
    Usuwa grę
    """
    pass

async def get_all_games(collection) -> List[GameOut]:
    """
    Zwraca listę gier
    """
    games = await collection.find({}).to_list(length=None)
    return [GameOut.from_mongo_result(game) for game in games]
