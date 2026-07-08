import pytest
from components.browser import Browser

@pytest.fixture
def driver():
    browser = Browser()
    browser.start()

    yield browser.driver

    browser.stop()
