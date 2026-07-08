from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from components.config import Config

class Browser:
    driver = None

    def start(self):
        options = webdriver.ChromeOptions()

        if Config.headless():
            options.add_argument("--headless")

        options.add_experimental_option('prefs', {
            'intl.accept_languages': 'ru',
        })

        service = ChromeService(ChromeDriverManager().install())

        self.driver = webdriver.Chrome(options, service)

        window_size = Config.window_size()

        if len(window_size) == 2:
            self.driver.set_window_size(window_size[0], window_size[1])
        else:
            self.driver.maximize_window()

    def stop(self):
        self.driver.quit()
