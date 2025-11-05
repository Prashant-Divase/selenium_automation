import  pytest,requests
from pages.login_page import LoginPage


@pytest.mark.login
def test_login_valid(driver,config):
    login = LoginPage(driver,
                      config)
    data=  {'username':'prashatn.divase@benisontech.com',
           'password':"Test"}
    login.open_url()
