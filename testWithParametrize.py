import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


@pytest.mark.parametrize('page', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_guest_should_see_login_link(browser, page):
    browser.implicitly_wait(10)
    link = f'https://stepik.org/lesson/{page}/step/1'
    browser.get(link)

    textArea = browser.find_element_by_css_selector('.textarea')
    answer = str(math.log(int(time.time())))
    textArea.send_keys(answer)

    btn = browser.find_element_by_css_selector('.submit-submission')
    btn.click()
    time.sleep(1)

    checkedText = browser.find_element_by_css_selector('.smart-hints__hint').text

    assert checkedText == 'Correct!'