from selenium import webdriver
import os
import time

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x1 = browser.find_element_by_name('firstname')
    x2 = browser.find_element_by_name('lastname')
    x3 = browser.find_element_by_name('email')
    x1.send_keys('213')
    x2.send_keys('213')
    x3.send_keys('213')

    inputfile = browser.find_element_by_css_selector('#file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test4.txt')   
    inputfile.send_keys(file_path)

    btn = browser.find_element_by_css_selector('.btn-primary')
    btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()