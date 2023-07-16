from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

def calc(x): return math.log(abs(12* math.sin(x))) #Посчитать математическую функцию от x.
    

try:
    link = "https://suninjuly.github.io/execute_script.html" #Открыть страницу https://SunInJuly.github.io/execute_script.html.
    browser = webdriver.Chrome()
    browser.get(link)
    
   
	
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value") #Считать значение для переменной x.
    x = x_element.text
    x = int(x)
    y = calc(x)
    

    
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer") #Ввести ответ в текстовое поле.
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(y)
    
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox") #Выбрать checkbox "I'm the robot".
    #browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
    option1.click()
    
    option12 = browser.find_element(By.CSS_SELECTOR, "#robotsRule") #Переключить radiobutton "Robots rule!".
    #browser.execute_script("return arguments[0].scrollIntoView(true);", option12)
    option12.click()
    
    button = browser.find_element(By.CSS_SELECTOR, ".btn") #Нажать на кнопку "Submit".
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
   
	
finally:
  # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
