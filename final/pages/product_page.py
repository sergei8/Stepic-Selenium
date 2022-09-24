from re import L
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
            
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        add_to_basket_button.click()
        
    def shuld_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), 'Add to basket button is not present'
        
    