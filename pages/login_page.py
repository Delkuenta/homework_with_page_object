from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url.find("/login") > 0, \
            "Warning: incorrect link"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), \
            "Warning: element Login Username not found"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Warning: element Login Password not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), \
            "Warning: element Registration email not found"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD1), \
            "Warning: element Registration Password(first) not found"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD2), \
            "Warning: element Registration Password(second) not found"

    def register_new_user(self, email, password):
        registration_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        registration_email.send_keys(email)
        password_input1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        password_input1.send_keys(password)
        password_input2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        password_input2.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        registration_button.click()