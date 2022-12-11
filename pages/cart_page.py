from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class CartPage(BasePage):
    B_PLACE_ORDER = (
        By.XPATH, "//button[contains(text(),'Place Order')]")
    F_NAME = (By.ID, "name")
    F_COUNTRY = (By.ID, "country")
    F_CITY = (By.ID, "city")
    F_CREDIT_CARD = (By.ID, "card")
    F_MONTH = (By.ID, "month")
    F_YEAR = (By.ID, "year")

    def place_order(self):
        self.wait_until_clickable(self.B_PLACE_ORDER).click()

    def fill_form(self, name, country, city, card, month, year):
        self.wait_until_clickable(self.F_NAME).send_keys(name)
        self.wait_until_clickable(self.F_COUNTRY).send_keys(country)
        self.wait_until_clickable(self.F_CITY).send_keys(city)
        self.wait_until_clickable(self.F_CREDIT_CARD).send_keys(card)
        self.wait_until_clickable(self.F_MONTH).send_keys(month)
        self.wait_until_clickable(self.F_YEAR).send_keys(year)
