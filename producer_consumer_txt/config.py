from pydantic import BaseSettings


class Envs(BaseSettings):
    PROJETO_NOME: str = "Producer Consumer Text"
    PROJETO_DESC: str = "API to send a json to a queue and be stored in a txt."

    class Config:
        case_sensitive = True


envs = Envs()
