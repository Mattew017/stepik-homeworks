from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
try:
    x = browser.find_element_by_css_selector("#input_value").text
    y = calc(x)

    input_field = browser.find_element_by_css_selector("input.form-control")
    input_field.send_keys(y)
    # находим кнопку
    button = browser.find_element_by_tag_name("button")

    # скролим вниз, чтобы она стала видна
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    checkbox = browser.find_element_by_css_selector("label[for='robotCheckbox']")
    checkbox.click()

    radiobox = browser.find_element_by_css_selector("input[id='robotsRule']")
    radiobox.click()
    # кликаем на кнопку
    button.click()



finally:
    time.sleep(7)
    browser.quit()
