from selenium import webdriver
from selenium.webdriver.common.by import By

import math
from time import sleep

link = "http://suninjuly.github.io/get_attribute.html"

with webdriver.Chrome() as browser:
    browser.get(link)
    value = browser.find_element_by_id('treasure').get_attribute('valuex')
    browser.find_element_by_id('answer').send_keys(str(math.log(abs(12*math.sin(int(value))))))
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element_by_css_selector('form button[type="submit"]').click()
    sleep(5)
