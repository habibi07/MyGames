from fastapi import FastAPI
from typing import List
from models import GameIn, GameOut

app = FastAPI()


@app.get('/games/{game_id}', response_model=GameOut)
async def get_game(game_id: str):
    """
    Zwraca informacje o grze
    """
    pass

@app.get('/games/', response_model=List[GameOut])
async def get_games():
    """
    Zwraca wszystkie gry
    """
    pass

@app.post('/games/', response_model=GameOut)
async def post_game(game: GameIn):
    """
    Pozwala dodać grę
    """
    pass

@app.delete('/game/{game_id}', status_code=204)
async def delete_game(game_id: str):
    """
    Usuwa grę
    """
    pass

@app.put('/game/{game_id}', response_model=GameOut)
async def put_game(game: GameIn, game_id: str):
    """
    Pozwala zmodyfikować grę
    """
    pass

