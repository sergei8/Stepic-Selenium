import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep, time
import math
from typing import List

links = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1',
]
    
@pytest.mark.parametrize('link', links)
def test_alliens_message(browser: webdriver.Chrome, link: List[str]):
    aliens_message = ''
    
    browser.get(link)
    
    answer = str(math.log(int(time())))
    
    answer_field = WebDriverWait(browser, 10) \
        .until(EC.element_to_be_clickable((By.CLASS_NAME, 'ember-text-area'))) 
    answer_field.send_keys(answer)

    submit = WebDriverWait(browser, 10) \
        .until(EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission')))
    submit.click()
    
    result = WebDriverWait(browser, 10) \
        .until(EC.element_to_be_clickable((By.CLASS_NAME, 'smart-hints__hint'))) \
        .text
    
    try:
        assert result == 'Correct!'
    except:
        aliens_message += f'{result}'
        print (aliens_message)

    sleep(1)
