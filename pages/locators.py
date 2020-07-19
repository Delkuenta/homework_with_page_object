from selenium.webdriver.common.by import By


class ProductPageLocators:
    ADD_BASKET_BUTTON = (By.XPATH, "//button[@value='Добавить в корзину']")

    NAME_PRODUCT_IN_DESCRIPTION = (By.XPATH, "//div[@id='content_inner']/article/div/div[2]/h1")
    PRICE_PRODUCT_IN_DESCRIPTION = (By.XPATH, "//article/div/div[2]/p")
    NAME_PRODUCT_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRICE_PRODUCT_IN_MESSAGE = (By.CSS_SELECTOR, "#content_inner .price_color")

