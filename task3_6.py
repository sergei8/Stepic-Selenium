import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep, time
import math
from typing import List

links = [
    'https://stepik.org/lesson/236895/step/1',
    # 'https://stepik.org/lesson/236896/step/1',
    # 'https://stepik.org/lesson/236897/step/1',
    # 'https://stepik.org/lesson/236898/step/1',
    # 'https://stepik.org/lesson/236899/step/1',
    # 'https://stepik.org/lesson/236903/step/1',
    # 'https://stepik.org/lesson/236904/step/1',
    # 'https://stepik.org/lesson/236905/step/1',
]

    
@pytest.mark.parametrize('link', links)
def test_alliens_message(browser:webdriver.Chrome, link: List[str]):
    browser.get(link)
    
    browser.implicitly_wait(10)    
    answer = str(math.log(int(time())))
    browser.find_element(By.ID, 'ember87').send_keys(answer)
    
    browser.implicitly_wait(10)    
    submit = browser.find_element(By.TAG_NAME, 'button')
    submit.click()
    sleep(5)
    result = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text
    
    assert result == 'Correct!'
    sleep(10)
    
    
    pass
