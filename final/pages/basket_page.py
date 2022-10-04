from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class BasketPage(BasePage):
    
    def basket_should_be_empty(self):
        basket_content = self.browser.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/p")
        assert 'Your basket is empty' in basket_content.text

