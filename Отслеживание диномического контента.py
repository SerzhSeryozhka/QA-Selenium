from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Создаем экземпляр драйвера
driver = webdriver.Chrome()

# Открываем страницу
driver.get("https://erikdark.github.io/QA_autotest_16/")

# Ждем, пока цена Лады станет 550 долларов
wait = WebDriverWait(driver, 10)
price_element = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#car-card"), "550"))

# Нажимаем на кнопку
button = driver.find_element(By.CSS_SELECTOR, "button")
button.click()

# Проверяем текст в блоке
result_text = driver.find_element(By.CSS_SELECTOR, "#result").text
assert result_text == "Wonderful!"

# Ждем 5 секунд, затем закрываем браузер
time.sleep(5)
driver.quit()
