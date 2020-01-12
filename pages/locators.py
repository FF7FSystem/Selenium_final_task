from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_FORM = (By.XPATH, "//form[@id='login_form']")
    REG_FORM = (By.XPATH, "//form[@id='register_form']")
    INPUT_EMAIL = (By.XPATH, "//input[@name='registration-email']")
    INPUT_PASSWORD_1 = (By.XPATH, "//input[@name='registration-password1']")
    INPUT_PASSWORD_2 = (By.XPATH, "//input[@name='registration-password2']")
    REG_BUTTON = (By.XPATH, "//button[@name='registration_submit']")


class BasketPageLocators():
    BASKET_LINK = (By.XPATH, "//button[contains(@class,'add-to-basket')]")
    BOOK_NAME = (By.XPATH, "//h1")
    CONFIRM_BOOK_NAME = (By.XPATH, "//strong[text()=//h1/text()]")
    BOOK_PRICE = (By.XPATH, "//p[@class='price_color']")
    CONFIRM_BOOK_PRICE = (By.XPATH, "//strong[contains(text(),//p[@class='price_color'])]")
    LINK_OF_ITEMS = (By.XPATH, "//div[@class='basket-items']/div[@class='row']")
    MESS_BASKET_EMPTY = (By.XPATH,"//div[@id='content_inner']/p")

class ProductPageLocators():
    SUCCESS_MESSAGE = (By.XPATH, "//strong[text()='Deferred benefit offer']")
    LOGIN_LINK = (By.XPATH, "//a[@id='login_link']")
    MINI_BASKET = (By.XPATH, "//div[contains(@class,'basket-mini')]")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc") #для проверки что тест может упасть
    BASKET_LINK_IN_HEAD = (By.XPATH, "(//a[contains(@href,'/basket/')])[1]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")