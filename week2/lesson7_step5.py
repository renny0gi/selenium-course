from selenium import webdriver

import math
from time import sleep

link = "http://suninjuly.github.io/math.html"

with webdriver.Chrome() as browser:
    browser.get(link)
    value = browser.find_element_by_id('input_value').text
    browser.find_element_by_id('answer').send_keys(str(math.log(abs(12*math.sin(int(value))))))
    browser.find_element_by_css_selector('[for="robotCheckbox"]').click()
    browser.find_element_by_css_selector('[for="robotsRule"]').click()
    browser.find_element_by_css_selector('form > button').click()
    sleep(5)
