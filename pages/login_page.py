from http.client import responses

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import logging,requests
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger('pytest-automation')

class LoginPage(BasePage):
    def __init__(self,driver,config):
        super().__init__(driver)
        self.url = config['base_url']
        self.password = config['password']
        self.driver.implicitly_wait(10)

    def open_url(self):
        logger.info(f"Opening URL in {self.url}")
        # self.driver.find_element(By.XPATH)
        self.driver.get(self.url)





