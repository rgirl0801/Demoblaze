from typing import Tuple

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    B_CAROUSEL_NEXT = (
        By.XPATH, "//body/nav[@id='narvbarx']/div[@id='contcar']/div[@id='carouselExampleIndicators']/a[2]/span[1]")
    B_CAROUSEL_PREV = (
        By.XPATH, "//span[contains(text(),'Previous')]")

    def carousel_click_next(self):
        self.wait_until_clickable(self.B_CAROUSEL_NEXT).click()

    def carousel_click_prev(self):
        self.wait_until_clickable(self.B_CAROUSEL_PREV).click()

    def kate1(self):
        element = self.browser.find_element(self.B_CAROUSEL_PREV)
        self.browser.execute_script("arguments[0].click();", element)

    def kate2(self):
        self.wait_until_clickable(self.B_CAROUSEL_PREV).send_keys('<')
