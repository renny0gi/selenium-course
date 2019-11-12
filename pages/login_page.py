from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, f'Current page is not {self.__class__.__name__}'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            f'Login form is not presented on {self.__class__.__name__}'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            f'Registration form is not presented on {self.__class__.__name__}'

    def register_new_user(self, email, password):
        self.should_be_login_form()
        self.browser.find_element(*LoginPageLocators.EMAIL_REGISTER_FORM).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASS_REGISTER_FORM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASS_REGISTER_FORM_CONFIRM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.SUBMIT_LOGIN_FORM).click()