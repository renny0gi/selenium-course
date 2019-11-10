import time

from pages.main_page import MainPage
from pages.login_page import LoginPage


link = 'http://selenium1py.pythonanywhere.com/'
# link = ' http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer'

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link).open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link).open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

# def test_check_login_page(browser):
#     link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
#     page = LoginPage(browser, link).open()
#     page.should_be_login_page()