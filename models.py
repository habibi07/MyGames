from pydantic import BaseModel, Field 

class GameBase(BaseModel):
    name: str = Field(..., title="Game name", max_length=20)
    producer: str = Field(..., title="Game producer", max_length=20)

class GameIn(GameBase):
    """
    Game input model
    """
    pass

class GameOut(GameBase):
    """
    Game output model
    """
    id: str = Field(None, title="Game ID")

    @classmethod
    def from_mongo_result(cls, data):
        """
        Tworzy obiekt tej klasy na podstawie odpowiedzi 
        z mongodb
        """
        if not data:
            return data
        id = data.pop('_id', None)
        return cls(**dict(data, id=str(id)))

