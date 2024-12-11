import pytest
from seleniumbase import BaseCase


class App:
    default_timeout = 2000
    home_screen_timeout = 5000

    def __init__(self):
        self.app_frontend: BaseCase = pytest.app_frontend
