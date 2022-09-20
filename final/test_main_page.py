import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def test_add_button(browser: webdriver.Chrome):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
    
    # sleep(10)

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()