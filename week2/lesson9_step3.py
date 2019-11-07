from selenium import webdriver
from selenium.webdriver.common.by import By

import math
from time import sleep

link = "http://suninjuly.github.io/alert_accept.html"

with webdriver.Chrome() as browser:
    browser.get(link)
    browser.find_element(By.TAG_NAME, 'button').click()
    browser.switch_to.alert.accept()
    value = int(browser.find_element_by_id('input_value').text)
    browser.find_element_by_id('answer').send_keys(str(math.log(abs(12*math.sin(value)))))
    browser.find_element_by_css_selector('form button[type="submit"]').click()
    print(browser.switch_to.alert.text.split()[-1])

