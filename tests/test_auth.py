import allure
import pytest

from constants import POSITIVE_LOGIN_CREDS, POSITIVE_SIGNUP_CREDS, NEGATIVE_LOGIN_CREDS
from pages.main_page import MainPage


class TestAuthClass:
    @pytest.fixture(autouse=True)
    def setup(self, browser, url):
        self.main_page = MainPage(browser, url)
        self.main_page.open_page()

    @allure.feature('Login on UI')
    def test_login_ui(self):
        self.main_page.go_to_login()
        self.main_page.login_ui(POSITIVE_LOGIN_CREDS['name'], POSITIVE_LOGIN_CREDS['password'])
        self.main_page.check_login_successfully_complete()

    @allure.feature('Sign up on UI')
    def test_signup_ui(self):
        self.main_page.go_to_signup()
        self.main_page.signup_ui(POSITIVE_SIGNUP_CREDS['name'], POSITIVE_SIGNUP_CREDS['password'])
        self.main_page.check_signup_successfully_complete()

    @allure.feature('Negative login')
    @pytest.mark.parametrize("name, password", NEGATIVE_LOGIN_CREDS,
        ids=["empty name", "empty password",
             "unregistered user"])
    def test_login_negative(self, name, password):
        self.main_page.go_to_login()
        self.main_page.login_ui(name, password)
        self.main_page.check_login_impossible()
