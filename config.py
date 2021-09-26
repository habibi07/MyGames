import os
from pydantic import (
    AnyUrl,
    BaseSettings,
)

class MongoDsn(AnyUrl):
    """
    Typ danych do budowania i walidacji data source name 
    dla mongodb
    """
    allowed_schemes = { 'mongodb' }
    user_required = True

class Settings(BaseSettings):
    """
    Ustawienia aplikacji
    mongo_dsn - jest wymagane, pozostałe parametry
                przyjmują domyslne wartości
    """
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = False

    mongo_dsn: MongoDsn
    db_name: str = 'mygames'
    col: str = 'games'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

