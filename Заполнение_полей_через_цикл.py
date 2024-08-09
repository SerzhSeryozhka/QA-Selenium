from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try:
# Инициализация драйвера браузера (в данном случае Google Chrome)
    driver = webdriver.Chrome()
# Открываем указанную страницу
    driver.get("https://erikdark.github.io/Qa_autotest_03/")

# Находим все поля ввода и кнопку на странице
    input_fields = driver.find_elements(By.CSS_SELECTOR, "input")
    button = driver.find_element(By.CSS_SELECTOR, "button")
# Список значений для ввода в поля
    znach_poley = ['Ya', 'Yayay', 'yoyoy@yoyk.com',"+78887776655", 'Там же']
# Заполняем поля ввода
    for field, val in zip(input_fields, znach_poley):
        # time.sleep(0.00000005)
        field.send_keys(val)
# Нажимаем на кнопку
    time.sleep(0.5)
    button.click()
    time.sleep(0.5)
finally:

# Закрываем браузер
    driver.quit()