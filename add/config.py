import os


class Config:
    URL = os.getenv("BASE_URL", "https://stellarburgers.nomoreparties.site")
    # Test account for login / logout flows — set via environment, never hard-coded
    TEST_EMAIL = os.getenv("TEST_EMAIL")
    TEST_PASSWORD = os.getenv("TEST_PASSWORD")
