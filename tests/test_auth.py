import time
import pytest

from pages.cart_page import CartPage
from pages.main_page import MainPage
from constants import POSITIVE_LOGIN_CREDS


class TestAuthClass:
    @pytest.fixture(autouse=True)
    def setup(self, browser, url):
        self.main_page = MainPage(browser, url)
        self.main_page.open_page()

    def test_login_ui(self):
        self.main_page.go_to_login()
        self.main_page.login_ui(POSITIVE_LOGIN_CREDS['name'], POSITIVE_LOGIN_CREDS['password'])
