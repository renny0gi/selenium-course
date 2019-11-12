import time
import pytest

from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

BASIC_PROMO_URL = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'

list_of_urls = [f'{BASIC_PROMO_URL}/?promo=offer{num}' for num in range(10)]
# Mark 8-th url as xfail since we know it's not gonna be fixed any time soon
list_of_urls[7] = pytest.param(list_of_urls[7], marks=pytest.mark.xfail)

def test_guest_can_see_product_info(browser):
    url_product_promo = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    product_page = ProductPage(browser, url_product_promo).open()
    product_page.should_be_product_name()
    product_page.should_be_product_price()
    product_page.should_be_product_description

@pytest.mark.parametrize('url_product_promo', list_of_urls)
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, url_product_promo):
    product_page = ProductPage(browser, url_product_promo).open()

    name = product_page.get_product_name()
    print(f'{name=}')
    price = product_page.get_product_price()
    print(f'{price=}')
    product_page.should_be_button_add_to_basket()
    product_page = product_page.add_to_basket()
    
    product_page.solve_quiz_and_get_code()
    
    product_page.check_add_msg_with_product_name(name)
    product_page.check_add_msg_with_basket_sum(price)
    
@pytest.mark.xfail(reason='Provided the product exist user will see the success msg')
@pytest.mark.negative_tests
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, BASIC_PROMO_URL).open()
    product_page = product_page.add_to_basket()
    product_page.should_not_be_success_message()

@pytest.mark.negative_tests
def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, BASIC_PROMO_URL).open()
    product_page.should_not_be_success_message()

@pytest.mark.skip(reason='this isn\'t implemented yet')
@pytest.mark.negative_tests
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, BASIC_PROMO_URL).open()
    product_page = product_page.add_to_basket()
    product_page.should_disappear_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link).open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.check_basket
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link).open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_empty = 'Your basket is empty. Continue shopping'
    basket_page.should_see_text_empty_basket()
    basket_page.check_text_empty_basket(basket_empty)

class TestUserAddToBasketFromProductPage:

    url = list_of_urls[0]

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        login_link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        login_page = LoginPage(browser, login_link).open()
        login_page.register_new_user(self._generate_email(), 'testpass123')
        login_page.should_be_authorized_user()

    def _generate_email(self):
        return str(time.time()) + "@fakemail.org"
    
    @pytest.mark.negative_tests
    def test_guest_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, self.url).open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, self.url).open()

        name = product_page.get_product_name()
        price = product_page.get_product_price()
        product_page.should_be_button_add_to_basket()
        product_page = product_page.add_to_basket()
        
        product_page.solve_quiz_and_get_code()
        product_page.check_add_msg_with_product_name(name)
        product_page.check_add_msg_with_basket_sum(price)