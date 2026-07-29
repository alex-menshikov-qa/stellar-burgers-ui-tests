import os


class Config:
    URL = os.getenv("BASE_URL", "https://stellarburgers.nomoreparties.site")