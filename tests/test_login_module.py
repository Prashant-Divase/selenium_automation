from pages.login_page import LoginPage
import  pytest


class TestLogin:

    def test_login(self,driver,config):
        login = LoginPage(driver, config)
        login.open_url()