from pydantic import BaseSettings


class Envs(BaseSettings):
    PROJECT_NAME: str = "Producer Consumer Text"
    PROJECT_DESC: str = "API to send a json to a queue and be stored in a txt."

    SAVE_LOG: bool = True

    BROKER: str
    BACKEND: str

    class Config:
        case_sensitive = True


envs = Envs()
