from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math

class ProductPage(BasePage):
            
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        add_to_basket_button.click()
        self.solve_quiz_and_get_code()

    def shuld_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), 'Add to basket button is not present'
     
    def choosen_product_name_is_correct(self):
        product_name_in_basket = self.browser.find_element(By.CSS_SELECTOR, '.alertinner strong')
        product_name = self.browser.find_element(By.CSS_SELECTOR, '.product_main h1')
        assert product_name_in_basket.text == product_name.text, 'product name has choosen incorrect'

    def choosen_product_price_is_correct(self):
        product_price_in_basket = self.browser.find_element(By.CSS_SELECTOR, '.alertinner p strong')
        product_price = self.browser.find_element(By.CSS_SELECTOR, '.product_main > p')
        assert product_price_in_basket.text == product_price.text, 'product price has choosen incorrect'
            
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED_SUCCESS), \
        "Success message is presented, but should not be"
    
    def should_disapeared_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED_SUCCESS), \
        "Success message is presented, but should not be"
        
    # TODO
    def test_guest_should_see_login_link_on_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()       
        
             
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")