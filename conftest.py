import pytest
from components.browser import Browser

@pytest.fixture
def driver():
    browser = Browser()
    browser.start()

    yield browser.driver

    browser.stop()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get('driver')
        driver.save_screenshot('latest.png')
