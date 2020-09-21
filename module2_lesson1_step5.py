from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #задать функцию y
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    #найти x
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    #ввести ответ
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    
    #поставить checkbox
    check1 = browser.find_element_by_css_selector("#robotCheckbox")
    check1.click()

    #поставить radiobutton
    radio1 = browser.find_element_by_css_selector("#robotsRule")
    radio1.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()