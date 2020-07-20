from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BASKET_BUTTON), "Add Basket Button is not presented"

    def should_be_correct_name(self):
        assert self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_DESCRIPTION).text == \
               self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_MESSAGE).text, \
            "Basket name message does not match the item name"

    def should_be_correct_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_IN_DESCRIPTION).text == \
               self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_IN_MESSAGE).text, \
            "Basket price message does not match the item price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should dissapeared"
