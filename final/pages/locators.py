from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM_ID = (By.ID, "login_form")
    REGISTER_FORM_ID = (By.ID, "register_form")
    
class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    