from selenium import webdriver
import time

try:
    link = "https://planoplan.com/"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.set_window_size(1900, 1200)
    # Кликаем кнопку войти и начинаем регистрацию
    buttonJoin = browser.find_element_by_css_selector('.widget-button__ButtonText-sc-7ezmr3-4.kGpZKe')
    buttonJoin.click()

    time.sleep(1)
    button_reg = browser.find_element_by_css_selector('.link__View-sc-1ydrjtx-0')
    button_reg.click()
    time.sleep(1)
    input2 = browser.find_element_by_name('username')
    input2.send_keys('VasiliiZaicev2@mail.ru')
    time.sleep(2)
    input3 = browser.find_element_by_xpath('//*[@id="form-entry"]/div/form/fieldset[2]/label/div[2]/input').send_keys('dasdasdzx3')


    button = browser.find_element_by_css_selector(".cCelhz")
    button.click()
    time.sleep(1)
    # Подтверждаем почту
    browser.get(link)
    # input4 = browser.find_element_by_css_selector('.//*[@id="form-entry"]/div/form/fieldset/label/div[2]/input')
    # input4.send_keys('578255')

    # buttonConfirm = browser.find_element_by_css_selector('.iWHvdP')
    # buttonConfirm.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы


finally:
    #выключаем браузер после
    time.sleep(5)
    browser.quit()