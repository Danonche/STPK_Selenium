from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x): return math.log(abs(12* math.sin(x))) #Посчитать математическую функцию от x.

try:
    link = "http://suninjuly.github.io/redirect_accept.html" #Открыть страницу http://suninjuly.github.io/redirect_accept.html.
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element(By.CSS_SELECTOR, ".btn") #Нажать на кнопку "Submit".
    button.click()
    
    browser.switch_to.window(browser.window_handles[1])
    
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value") #Считать значение для переменной x.
    x = x_element.text
    x = int(x)
    y = calc(x)
    
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer") #Ввести ответ в текстовое поле.
    input1.send_keys(y)
    
    button = browser.find_element(By.CSS_SELECTOR, ".btn") #Нажать на кнопку "Submit".
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
finally:
  # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываю браузер после всех манипуляций
    browser.quit()