from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
try:
    x = browser.find_element_by_css_selector("#input_value").text
    y = calc(x)
    input_field = browser.find_element_by_css_selector("input.form-control")
    input_field.send_keys(y)

    checkbox = browser.find_element_by_css_selector("label[for='robotCheckbox']")
    checkbox.click()

    radiobox = browser.find_element_by_css_selector("label[for='robotsRule']")
    radiobox.click()

    submit_btn = browser.find_element_by_css_selector("button[type='submit']")
    submit_btn.click()


finally:
    time.sleep(7)
    browser.quit()
