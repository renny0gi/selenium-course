import unittest
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestBasic(unittest.TestCase):

    expected = 'Congratulations! You have successfully registered!'

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def do_job(self, url):
        self.browser.get(url)

        self.browser.find_element_by_css_selector("input.first[required]").send_keys("Vasya")
        self.browser.find_element_by_css_selector("input.second[required]").send_keys("Pupkin")
        self.browser.find_element_by_css_selector("input.third[required]").send_keys("Vasya@stepik.org")
        self.browser.find_element_by_css_selector('button[type="submit"]').click()

        WebDriverWait(self.browser, 5).until(
            EC.url_contains('registration_result'))

        return self.browser.find_element_by_tag_name("h1").text

        
    def test_registration(self):
        url = f'http://suninjuly.github.io/registration1.html'
        actual = self.do_job(url)
        self.assertEqual(self.expected, actual, f'should be {self.expected}, but found {actual}')
        time.sleep(2)

    
    def test_registration2(self):
        url = 'http://suninjuly.github.io/registration2.html'
        actual = self.do_job(url)
        self.assertEqual(self.expected, actual, f'should be {self.expected}, but found {actual}')
        time.sleep(2)
  

if __name__ == "__main__":
    unittest.main()
