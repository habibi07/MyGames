from typing import List

from models import GameIn, GameOut

async def get_game_by_id(collection, game_id: str) -> GameOut:
    """
    Zwraca pojedyńczą grę na podstawie id lub wyrzuca błað gdy 
    gry nie znaleziono
    """
    pass

async def insert_game(collection, game: GameIn) -> GameOut:
    """
    Dodaje grę do kolekcji
    """
    pass

async def update_game(collection, game: GameIn, game_id: str) -> GameOut:
    """
    Aktualizuje istniejącą grę
    """
    pass

async def save_game(collection, game: GameIn, game_id: str = None) -> GameOut:
    """
    Zapis lub aktualizacja gry
    """
    pass

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
