from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x): return math.log(abs(12* math.sin(x)))

try:
    browser = webdriver.Chrome()

    browser.get("https://suninjuly.github.io/explicit_wait2.html")
    
    button = browser.find_element(By.CSS_SELECTOR, "#book")
    
    WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#price"),"$100")) # ждем нужный текст на странице
    
    button.click()
    
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value") #Считать значение для переменной x.
    x = x_element.text
    x = int(x)
    y = calc(x)
    
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer") #Ввести ответ в текстовое поле.
    input1.send_keys(y)
    
    button2 = browser.find_element(By.CSS_SELECTOR, "#solve") #Нажать на кнопку "Submit".
    
    button2.click()

finally:
  # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываю браузер после всех манипуляций
    browser.quit()