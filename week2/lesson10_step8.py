from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import math
from time import sleep

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(value):
    return math.log(abs(12*math.sin(value)))

with webdriver.Chrome() as browser:
    browser.get(link)
    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )

    browser.find_element(By.ID, 'book').click()
    value = int(browser.find_element_by_id('input_value').text)
    browser.find_element_by_id('answer').send_keys(str(calc(value)))
    browser.find_element_by_css_selector('form button[type="submit"]').click()
    print(browser.switch_to.alert.text.split()[-1])