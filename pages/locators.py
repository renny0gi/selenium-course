from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'id_login-password')
    EMAIL_REGISTER_FORM = (By.ID, 'id_registration-email')
    PASS_REGISTER_FORM = (By.ID, 'id_registration-password1')
    PASS_REGISTER_FORM_CONFIRM = (By.ID, 'id_registration-password2')
    SUBMIT_LOGIN_FORM = (By.NAME, 'registration_submit')


class ProductPageLocators:
    ADD_BASKET = (By.CSS_SELECTOR, 'form#add_to_basket_form button[type="submit"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_DESCR = (By.CSS_SELECTOR, '#product_description + p')
    SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, '#messages .alert:first-child strong')
    SUCCESS_MESSAGE_BASKET_SUM = (By.CSS_SELECTOR, '#messages .alert:last-child strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > div')

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini .btn-group > a.btn')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    TEXT_EMPTY_BASKET = (By.CSS_SELECTOR, '.content #content_inner > p')
    BASKET_ITEMS = (By.CSS_SELECTOR, '.content #content_inner .basket-items')