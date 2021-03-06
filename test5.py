from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    btn1 = browser.find_element_by_css_selector('.trollface')
    btn1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = int(browser.find_element_by_css_selector('#input_value').text)
    y = calc(x)

    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys(y)

    btn = browser.find_element_by_css_selector('.btn-primary')
    btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()