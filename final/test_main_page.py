import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    
def test_gest_should_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page_link = browser.current_url
    login_page = LoginPage(browser, login_page_link)
    login_page.should_be_login_form()
    
def test_gest_should_see_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page_link = browser.current_url
    login_page = LoginPage(browser, login_page_link)
    login_page.should_be_login_form()
    
def test_correct_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page_link = browser.current_url
    login_page = LoginPage(browser, login_page_link)
    login_page.should_be_login_url(login_page_link)
