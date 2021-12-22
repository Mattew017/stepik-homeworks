from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
try:
    num_1 = int(browser.find_element_by_id("num1").text)
    num_2 = int(browser.find_element_by_id("num2").text)
    select = Select(browser.find_element_by_tag_name("select"))
    y = select.select_by_value(str(num_1 + num_2))  # ищем элемент с текстом "Python"
    print(y)
    submit_btn = browser.find_element_by_css_selector("button[type='submit']")
    submit_btn.click()


finally:
    time.sleep(5)
    browser.quit()
