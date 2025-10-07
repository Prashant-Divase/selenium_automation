from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self,driver):
        self.driver =driver
        self.wait = WebDriverWait(driver,10)

    def click(self,xpath):
        self.wait.until(EC.element_to_be_clickable(xpath)).click()

