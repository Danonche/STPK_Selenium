from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time


try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)                       # кликаю по ссылке
    
    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")   # Нахожу элемент по селектору #num1
    x = x_element.text  # записываю в переменную x найденное строковое значение 
    
   
    y_element = browser.find_element(By.CSS_SELECTOR, "#num2") # Нахожу элемент по селектору #num1
    y = y_element.text # записываю в переменную y найденное строковое значение
    
    sum_el = int(x) + int(y)  #чтобы выполнить сложение нужно перевести все значения в int
    
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(value = str(sum_el)) 
    
  
    button = browser.find_element(By.CSS_SELECTOR, ".btn") # Нахожу элемент по селектору .btn
    button.click() # кликаю на кнопку 
finally:
  # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываю браузер после всех манипуляций
    browser.quit()