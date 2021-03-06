from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_css_selector('#input_value').text
    xres = math.log(abs(12 * math.sin(int(x))))
    browser.execute_script("window.scrollBy(0, 100);")
    inputForm= browser.find_element_by_xpath('//*[@id="answer"]')

    inputForm.send_keys(str(xres))

    browser.find_element_by_xpath('/html/body/div/form/div[2]/label').click()


    browser.find_element_by_xpath('/html/body/div/form/div[4]/label').click()

    browser.find_element_by_css_selector('.btn-primary').click()



finally:
    #выключаем браузер после
    time.sleep(4)
    browser.quit()