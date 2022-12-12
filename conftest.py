import pytest
import Links

import logging

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def browser():
    options = webdriver.ChromeOptions()
    options.headless = True
    logging.info('start logs')
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    browser.maximize_window()
    yield browser
    logging.info('end logs')
    browser.quit()


@pytest.fixture(scope="session")
def url():
    url = Links.base_url
    if not url:
        raise Exception("Wrong environment")
    return url
