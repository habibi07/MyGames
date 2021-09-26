from pydantic import BaseModel, Field 

class GameBase(BaseModel):
    name: str = Field(..., title="Game name", max_length=20)
    producer: str = Field(..., title="Game producer", max_length=20)

class GameIn(GameBase):
    pass

class GameOut(GameBase):
    id: str = Field(None, title="Game ID")
