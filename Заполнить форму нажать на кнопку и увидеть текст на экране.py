from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Создаем объект веб-драйвера для Chrome
driver = webdriver.Chrome()
time.sleep(0.5)

# Открываем страницу
driver.get("https://erikdark.github.io/checkbox_iterms-/")
time.sleep(0.5)

# Находим элементы формы
checkbox_1 = driver.find_element(By.ID, "check1").click()
checkbox_2 = driver.find_element(By.ID, "check2").click()
checkbox_2 = driver.find_element(By.ID, "check3").click()
submit_button = driver.find_element(By.CSS_SELECTOR, "button").click()
    # Ждем, пока появится элемент с текстом
wait = WebDriverWait(driver, 1)
result_text = wait.until(EC.presence_of_element_located((By.ID, "myModal"))).text
    # Выводим текст на экран
print(result_text)
    # Закрываем браузер
driver.quit()
