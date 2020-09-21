from selenium import webdriver
import time
import os
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'send_me.txt') 

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # input first name
    first = browser.find_element_by_css_selector("[name=firstname]")
    first.send_keys("Vasya")
    
    # input last name
    last = browser.find_element_by_css_selector("[name=lastname]")
    last.send_keys("Pupkin")

    # input email
    email = browser.find_element_by_css_selector("[name=email]")
    email.send_keys("test@mail.ru")

    # choose file
    file = browser.find_element_by_id("file")
    file.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()