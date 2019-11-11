from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_BASKET).click()
        return self

    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BASKET), \
            f'Button add to basket is not presented on {self.__class__.__name__}'

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_product_description(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_DESCR).text
    
    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), \
            f'Product name is not presented on {self.__class__.__name__}'
    
    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), \
            f'Product price is not presented on {self.__class__.__name__}'

    def should_be_product_description(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_DESCR), \
            f'Product description is not presented on {self.__class__.__name__}'
    
    def check_add_msg_with_product_name(self, product_name):
        msg_prod_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME).text
        assert product_name == msg_prod_name, \
            f'Added product "{product_name}" doesn\'t match choosen product "{msg_prod_name}"'

    def check_add_msg_with_basket_sum(self, basket_sum):
        msg_basket_sum = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_BASKET_SUM).text
        assert basket_sum == msg_basket_sum, \
            f'Basket total\'s expected to be: {basket_sum}, but we got: {msg_prod_name}'
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should disappear"