from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    def __init__(self,driver,config):
        super().__init__(driver)
        self.url = config['base_url']
        self.password = config['password']

    def open_url(self):
        self.driver.get(self.url)

