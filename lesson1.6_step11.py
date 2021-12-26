from selenium import webdriver
import time

try:
    first_link = "http://suninjuly.github.io/registration1.html"
    second_link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    # browser.get(first_link)
    browser.get(second_link)

    # Ваш код, который заполняет обязательные поля
    first_name_field = browser.find_element_by_css_selector("input.first:required")
    last_name_field = browser.find_element_by_css_selector("input.second:required")
    email_field = browser.find_element_by_css_selector("input.third:required")

    first_name_field.send_keys("Имя")
    last_name_field.send_keys("Фамилия")
    email_field.send_keys("mail@mail.su")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()