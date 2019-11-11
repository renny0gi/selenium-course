import time
import pytest

from pages.product_page import ProductPage

# url_product_promo = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
url_product_promo = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7'

list_of_urls = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", \
        marks=pytest.mark.xfail),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]

def test_guest_can_see_product_info(browser):
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
    time.sleep(5)
    
    product_page.check_add_msg_with_product_name(name)
    product_page.check_add_msg_with_basket_sum(price)
    