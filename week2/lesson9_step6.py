from selenium import webdriver
from selenium.webdriver.common.by import By

import math
from time import sleep

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(value):
    return math.log(abs(12*math.sin(value)))

with webdriver.Chrome() as browser:
    browser.get(link)
    browser.find_element(By.TAG_NAME, 'button').click()
    target = [win for win in browser.window_handles if win != browser.current_window_handle][0]
    browser.switch_to.window(target)
    value = int(browser.find_element_by_id('input_value').text)
    browser.find_element_by_id('answer').send_keys(str(calc(value)))
    browser.find_element_by_css_selector('form button[type="submit"]').click()
    print(browser.switch_to.alert.text.split()[-1])

