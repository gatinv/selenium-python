from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    #задать функцию y
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    #найти x
    x = browser.find_element_by_id("input_value").text
    y = calc(x)

    # input answer
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()