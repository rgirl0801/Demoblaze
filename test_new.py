import time
import pytest

from pages.main_page import MainPage


class TestAuthorizationClass:
    @pytest.fixture(autouse=True)
    def setup(self, browser, url):
        self.main_page = MainPage(browser, url)

    def test_carousel_next_prev(self):
        self.main_page.open_page()
        # self.main_page.samsung_is_present()
        # self.main_page.carousel_click_prev()
        self.main_page.nexus_is_present()
        self.main_page.laptop_is_present()



