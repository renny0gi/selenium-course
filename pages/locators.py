from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    ADD_BASKET = (By.CSS_SELECTOR, 'form#add_to_basket_form button[type="submit"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_DESCR = (By.CSS_SELECTOR, '#product_description + p')
    MSG_ADD_PRODUCT_NAME = (By.CSS_SELECTOR, '#messages .alert:first-child strong')
    MSG_ADD_BASKET_SUM = (By.CSS_SELECTOR, '#messages .alert:last-child strong')
