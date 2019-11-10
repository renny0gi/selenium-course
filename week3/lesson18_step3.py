import pytest
from time import time
from math import log

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

answer = ''

def compute():
    return str(log(int(time())))

@pytest.fixture(scope='module')
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
    print(f'\n{answer}')


BASIC_URL = 'https://stepik.org/lesson/{module}/step/1'
modules = [
     236895,
     236896,
     236897,
     236898,
     236899,
     236903,
     236904,
     236905
]
@pytest.mark.parametrize('module', modules)
def test_extraterrestrial(browser, module):
    global answer
    browser.get(BASIC_URL.format(module=module))
    textatea = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'textarea'))
    )
    textatea.send_keys(compute())
    # browser.find_element_by_tag_name('textarea').send_keys(compute())
    browser.find_element_by_class_name('submit-submission').click()
    res = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'pre.smart-hints__hint'))
    )
    try:
        assert 'Correct!' == res.text, f'<< {res.text} >>'
    except AssertionError as e:
        answer += res.text
        raise e

if __name__ == '__main__':
    with webdriver.Chrome() as br:
        test_extraterrestrial(br, modules[-1])