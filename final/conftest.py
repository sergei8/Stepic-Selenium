import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='lenguage choice')
    
### read otions from command line
@pytest.fixture
def language(request):
    return request.config.getoption("--language")

@pytest.fixture(scope="function")
def browser(language):
    
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
        
    print("\nstart browser for test..")
    # browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()
