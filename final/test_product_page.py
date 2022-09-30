import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from .pages.product_page import ProductPage
import re

product_page_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
# product_page_link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'

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


def test_product_price(browser):
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
    
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, product_page_link)
    page.open()
    page.go_to_login_page()

# TODO
def test_guest_cant_see_product_in_basket_opened_from_product_page():
    pass