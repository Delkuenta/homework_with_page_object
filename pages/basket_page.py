from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket_message(self):
        MESSAGE_ENG = "Your basket is empty."
        assert MESSAGE_ENG in self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE_IN_BASKET_PAGE).text.strip(), \
            f"Warning: Message '{MESSAGE_ENG}' not present"

    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_BASKET), "Basket not empty"
