from selenium.webdriver.common.by import By
from pages.base.user.page import UserPage

class IndexPage(UserPage):
    def open(self):
        super().open("")

    def assert_h1(self):
        super().assert_h1("Поступай и учись в ЮУрГУ!")

    def open_contacts(self):
        link = self.driver.find_element(By.LINK_TEXT, "КОНТАКТЫ")
        link.click()
