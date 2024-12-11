import pytest

from src.main.python.core.page_objects.app import App


class LoginScreen(App):
    # Selectors
    username_textbox_elem = "//input[@name='username']"
    password_textbox_elem = "//input[@name='password']"
    login_button_elem = "//button[@type='submit']"

    def __init__(self):
        self.app_frontend = pytest.app_frontend

    pass
