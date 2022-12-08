import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.main_page import MainPage


class TestAuthorizationClass:
    @pytest.fixture(autouse=True)
    def setup(self, browser, url):
        self.main_page = MainPage(browser, url)

    @pytest.mark.xfail
    def carousel_next_prev(self):
        self.main_page.open_page()
        time.sleep(1)
        self.main_page.carousel_click_next()
        self.main_page.carousel_click_next()
        self.main_page.carousel_click_next()
        self.main_page.carousel_click_next()



