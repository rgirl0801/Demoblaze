import pytest
import Links

import logging

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def browser(request, headless):
    options = webdriver.ChromeOptions()
    options.headless = headless
    logging.info('start logs')
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options
    )
    yield browser
    logging.info('end logs')
    browser.quit()


@pytest.fixture(scope="session")
def url():
    url = Links.base_url
    if not url:
        raise Exception("Wrong environment")
    return url


@pytest.fixture(scope='class')
def headless(request):
    return request.config.getoption("--headless")


def pytest_addoption(parser):
    parser.addoption(
        "--launch",
        default="chrome",
        help="define browser: chrome or firefox, --browser=chrome",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        help="headless mode on or off, --headless",
    )
