from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x1 = browser.find_element_by_css_selector('#num1').text
    x2 = browser.find_element_by_css_selector('#num2').text
    result =  int(x2) + int(x1)
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(result))
    
    btn = browser.find_element_by_css_selector('.btn-default')
    btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()