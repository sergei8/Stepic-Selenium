import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from final.pages.base_page import BasePage
from final.pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import re
import string
import random

product_page_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'

@pytest.mark.need_review
def test_guest_can_open_product_page(browser):
    page = ProductPage(browser, product_page_link)
    page.open()
    assert re.match(r"http:\/\/selenium1py\.pythonanywhere\.com\/.*catalogue", browser.current_url), "can't open product page"

def test_guest_should_see_basket_button(browser):
    product_page = ProductPage(browser, product_page_link)
    product_page.open()
    product_page.shuld_be_basket_button()

@pytest.mark.parametrize('product_page_link', 
                         ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_product_name(browser, product_page_link):
    product_page = ProductPage(browser, product_page_link)
    product_page.open()
    product_page.add_to_basket()
    product_page.choosen_product_name_is_correct()

def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, product_page_link)
    product_page.open()
    product_page.add_to_basket()
    product_page.choosen_product_price_is_correct()
    
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # Открываем страницу товара 
    product_page = ProductPage(browser, product_page_link)
    product_page.open()

    # Добавляем товар в корзину
    product_page.add_to_basket()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    '''
    Открываем страницу товара 
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present'''
    product_page = ProductPage(browser, product_page_link)
    product_page.open()
    product_page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    '''
    Открываем страницу товара
    Добавляем товар в корзину
    Проверяем, что нет сообщения об успехе с помощью is_disappeared'''
    
    # Открываем страницу товара 
    product_page = ProductPage(browser, product_page_link)
    product_page.open()

    # Добавляем товар в корзину
    product_page.add_to_basket()

    product_page.should_disapeared_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, product_page_link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page_link = browser.current_url
    basket_page = BasketPage(browser, basket_page_link)
    basket_page.basket_should_be_empty()


class TestUserAddToBasketFromProductPage():
    
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
                 
        login_page = LoginPage(browser, 'http://selenium1py.pythonanywhere.com/ru/accounts/login/')
        login_page.open()
        
        # generate random email & password
        email = ''.join(random.choice(string.ascii_lowercase) for _ in range(7)) + '@gmail.com'
        password = ''.join(random.choice(string.ascii_letters) for _ in range(10))
        
        login_page.register_new_user(email, password)

        login_page.should_be_authorized_user()
           
    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, product_page_link)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, product_page_link)
        product_page.open()
        product_page.add_to_basket()
        browser.implicitly_wait(3) 
        product_page.choosen_product_price_is_correct()
    