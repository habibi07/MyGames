from fastapi import FastAPI

app = FastAPI()


@app.get('/games/{game_id}')
async def get_game(game_id: str):
    """
    Zwraca informacje o grze
    """
    pass

@app.get('/games/')
async def get_games():
    """
    Zwraca wszystkie gry
    """
    pass

@app.post('/games/')
async def post_game():
    """
    Pozwala dodać grę
    """
    pass

@app.delete('/game/{game_id}')
async def delete_game(game_id: str):
    """
    Usuwa grę
    """
    pass

@app.put('/game/{game_id}')
async def put_game(game_id: str):
    """
    Pozwala zmodyfikować grę
    """
    pass

