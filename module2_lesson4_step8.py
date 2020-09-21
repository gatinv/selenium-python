from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(12)

    # price
    price = WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    book = browser.find_element_by_id("book")
    book.click()

    #задать функцию y
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    #найти x
    x = browser.find_element_by_id("input_value").text
    y = calc(x)

    #scrolldown
    browser.execute_script("window.scrollBy(0, 100);")

    # input answer
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_id("solve")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()