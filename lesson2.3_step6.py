from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
try:
    button = browser.find_element_by_tag_name("button")
    button.click()
    # переключимся на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_id("input_value").text
    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(calc(x))

    submit = browser.find_element_by_css_selector("button[type='submit']")
    submit.click()


finally:
    time.sleep(7)
    browser.quit()
