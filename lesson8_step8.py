from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html" #Открыть страницу http://suninjuly.github.io/file_input.html.
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element(By.CSS_SELECTOR, ".form-group :nth-child(2)") #Ввести ответ в текстовое поле.
    input1.send_keys("Даниил")
    
    input2 = browser.find_element(By.CSS_SELECTOR, ".form-group :nth-child(4)") #Ввести ответ в текстовое поле.
    input2.send_keys("Ларионов")
    
    input3 = browser.find_element(By.CSS_SELECTOR, ".form-group :nth-child(6)") #Ввести ответ в текстовое поле.
    input3.send_keys("dli92@gmail.com")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    element = browser.find_element(By.CSS_SELECTOR, "#file ")
    element.send_keys(file_path)
    
    button = browser.find_element(By.CSS_SELECTOR, ".btn") #Нажать на кнопку "Submit".
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
  # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываю браузер после всех манипуляций
    browser.quit()
