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
    B_PURCHASE_CONFIRM = (By.XPATH, "//button[contains(text(),'Purchase')]")
    SUCCESS_POPUP = (By.XPATH, "/html[1]/body[1]/div[10]/h2[1]")
    B_OK = (By.XPATH, "//button[contains(text(),'OK')]")

    def place_order(self):
        self.wait_until_clickable(self.B_PLACE_ORDER).click()

    def fill_form(self, name, country, city, card, month, year):
        self.wait_until_clickable(self.F_NAME).send_keys(name)
        self.wait_until_clickable(self.F_COUNTRY).send_keys(country)
        self.wait_until_clickable(self.F_CITY).send_keys(city)
        self.wait_until_clickable(self.F_CREDIT_CARD).send_keys(card)
        self.wait_until_clickable(self.F_MONTH).send_keys(month)
        self.wait_until_clickable(self.F_YEAR).send_keys(year)

    def confirm_purchase(self):
        self.wait_until_clickable(self.B_PURCHASE_CONFIRM).click()

    def ok_purchase(self):
        self.wait_until_clickable(self.B_OK).click()

    def text_in_popup(self):
        self.wait_until_visible(self.SUCCESS_POPUP)