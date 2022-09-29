from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM_ID = (By.ID, "login_form")
    REGISTER_FORM_ID = (By.ID, "register_form")
    
class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_name h1')
    PRODUCT_PRICE = (By.CLASS_NAME, 'price_color')
    PRODUCT_NAME_IN_BASKET =  (By.CSS_SELECTOR, '.alertinner strong')
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, '.alertinner p strong')
    PRODUCT_ADDED_SUCCESS = (By.CLASS_NAME, 'alert-success')
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    