from dataclasses import dataclass
from environs import Env

@dataclass
class TGbot:
    token: str

@dataclass
class Config:
    tg_bot: TGbot

def load_config(path: str|None = None) -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(tg_bot=TGbot(token=env("token")))

