from selenium import webdriver
import time
import math

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    #задать функцию y
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    #найти x
    x = browser.find_element_by_id("input_value").text
    y = calc(x)

    # input answer
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    
    #scrolldown
    browser.execute_script("window.scrollBy(0, 100);")
    
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