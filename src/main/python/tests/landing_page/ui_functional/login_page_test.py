import allure

from src.main.python.core.page_objects.landing_page.login_screen import LoginScreen
from src.main.python.tests.landing_page.landing_page_base_test import LandingPageBaseTest


class TestLoginPage(LandingPageBaseTest):
    test_data = ''

    def test_valid_user_login(self):
        with allure.step(f"STEP 1: Validate login page is open."):
            assert self.app.frontend.assert_title("OrangeHRM")
        with allure.step(f"STEP 2: Enter username."):
            self.app.frontend.send_keys(LoginScreen.username_textbox_elem, "Admin")
        with allure.step(f"STEP 3: Enter password."):
            self.app.frontend.send_keys(LoginScreen.password_textbox_elem, "admin123")
