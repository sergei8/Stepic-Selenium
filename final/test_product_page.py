import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from .pages.product_page import ProductPage

def test_guest_can_open_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    assert browser.current_url == link
    
def test_guest_should_see_basket_button(browser):
    product_page_link = browser.current_url
    product_page = ProductPage(browser, product_page_link)
    product_page.shuld_be_basket_button()
