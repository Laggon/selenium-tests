import pytest
from classes.browser import Browser

@pytest.fixture
def driver():
    browser = Browser()
    browser.start()

    yield browser.driver

    browser.stop()
