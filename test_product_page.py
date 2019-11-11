import time
import pytest

from pages.product_page import ProductPage

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
    