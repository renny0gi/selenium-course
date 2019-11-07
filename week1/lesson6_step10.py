from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"

with webdriver.Chrome() as browser:
    browser.get(link)

    input1 = browser.find_element_by_css_selector("input.first[required]")
    input1.send_keys("Vasya")
    input2 = browser.find_element_by_css_selector("input.second[required]")
    input2.send_keys("Pupkin")
    input3 = browser.find_element_by_css_selector("input.third[required]")
    input3.send_keys("Vasya@stepik.org")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()