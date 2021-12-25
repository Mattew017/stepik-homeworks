from selenium import webdriver
import time
import os

with open("file.txt", 'w') as file:
    file.write("aboba")

current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')   # добавляем к этому пути имя файла


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
try:
    inputs = browser.find_elements_by_css_selector("input")
    for i in inputs[:3]:
        i.send_keys("lol")
    inputs[-1].send_keys(file_path)
    submit_btn = browser.find_element_by_tag_name("button")
    submit_btn.click()
finally:
    time.sleep(7)
    browser.quit()
