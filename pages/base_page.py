import logging
from typing import Tuple


from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    LOGGER = logging.getLogger(__name__)
    B_HOME = (By.XPATH, "//body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]/li[1]/a[1]")
    B_CONTACT = (By.XPATH, "//a[contains(text(),'Contact')]")
    B_ABOUT = (By.XPATH, "//a[contains(text(),'About us')]")
    B_CART = (By.XPATH, "//a[@id='cartur']")
    B_LOGOUT = (By.XPATH, "//a[@id='logout2']")
    B_SIGN_UP = (By.XPATH, "//a[@id='signin2']")

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open_page(self):
        try:
            self.browser.get(self.url)
        except Exception as e:
            self.LOGGER.error(f"tException: {e}")

    def wait_until_clickable(self, locator: Tuple, timeout: int = 5) -> WebElement:
        try:
            return WebDriverWait(self.browser, timeout).until(
                ec.element_to_be_clickable(locator))
        except TimeoutException as e:
            self.LOGGER.error(f"TimeoutException: {e}")

    def go_to_home(self):
        self.wait_until_clickable(self.B_HOME).click()

    def go_to_contact(self):
        self.wait_until_clickable(self.B_CONTACT).click()
