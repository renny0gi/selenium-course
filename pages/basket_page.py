from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            'Should be empty basket, but found product items'

    def should_see_text_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_EMPTY_BASKET), \
            f'the text "{basket_empty}" not presented on {self.__class__.__name__}'

    def check_text_empty_basket(self, basket_empty):
        got_text = self.browser.find_element(*BasketPageLocators.TEXT_EMPTY_BASKET).text
        assert basket_empty == got_text, \
            f'Should see the text "{basket_empty}", but got "{got_text}" on {self.__class__.__name__}'
