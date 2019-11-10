from contextlib import suppress
import time

from selenium.common.exceptions import NoSuchElementException

url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_guest_should_see_button_add_to_basket(browser):
    browser.get(url)
    button = None
    with suppress(NoSuchElementException):
        button = browser.find_element_by_css_selector('form#add_to_basket_form button[type="submit"]')
    assert button is not None, "Button add to basket is not presented"
    time.sleep(3)
