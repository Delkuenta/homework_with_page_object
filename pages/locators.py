from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//span/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class ProductPageLocators:
    ADD_BASKET_BUTTON = (By.XPATH, "//div[2]/form/button")

    NAME_PRODUCT_IN_DESCRIPTION = (By.XPATH, "//div[@id='content_inner']/article/div/div[2]/h1")
    PRICE_PRODUCT_IN_DESCRIPTION = (By.XPATH, "//article/div/div[2]/p")
    NAME_PRODUCT_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRICE_PRODUCT_IN_MESSAGE = (By.CSS_SELECTOR, "#content_inner .price_color")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(1)")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_SUBMIT = (By.CSS_SELECTOR, "#login_form > button")

    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "#register_form > button")

class BasketPageLocators:
    EMPTY_MESSAGE_IN_BASKET_PAGE = (By.CSS_SELECTOR, "#content_inner > p")
    ITEM_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")