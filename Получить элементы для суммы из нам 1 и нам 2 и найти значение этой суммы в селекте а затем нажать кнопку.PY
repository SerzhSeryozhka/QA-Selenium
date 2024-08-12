from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try:
        # инициализация драйвера
    driver = webdriver.Chrome()
        # открытие страници
    time.sleep(2)
    driver.get('https://suninjuly.github.io/selects1.html')
        # находим элементы
    time.sleep(0.5)
    num1 = driver.find_element(By.ID, 'num1').text
    # print(num1)
    time.sleep(0.5)
    num2 = driver.find_element(By.ID, 'num2').text
    # print(num2)
    n1 = int(num1)
    n2 = int(num2)
    res= n1 + n2
    res = str(res)
    # print(res)
    time.sleep(0.5)
    dropdown = driver.find_element(By.ID, 'dropdown').click()
    time.sleep(0.5)
    value_el = driver.find_element(By.CSS_SELECTOR, f'[value="{res}"]')
    time.sleep(0.5)
    sbt = driver.find_element(By.CSS_SELECTOR,'[type="submit"]').click()
finally:
    time.sleep(3)
        # закрытие драйвера
    driver.quit()