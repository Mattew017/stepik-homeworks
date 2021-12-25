import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 15 секунд, пока цена не станет <= 100
    text = WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )
    button = browser.find_element_by_id("book")
    button.click()

    x = int(browser.find_element_by_id("input_value").text)
    y = calc(x)
    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(y)

    submit = browser.find_element_by_id("solve")
    submit.click()
finally:
    time.sleep(7)
    browser.quit()