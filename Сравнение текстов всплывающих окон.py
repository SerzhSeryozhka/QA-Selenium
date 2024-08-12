from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try:
# Создаем экземпляр драйвера
    driver = webdriver.Chrome()
    time.sleep(0.5)
    # Открываем сайт
    driver.get("https://erikdark.github.io/alert_confirm_prompt/")

    # Нажимаем на первую кнопку (Alert)
    time.sleep(2)
    alert_button = driver.find_element(By.CSS_SELECTOR, "button:nth-child(1)")
    alert_button.click()
    time.sleep(2)

    # Принимаем Alert
    alert = driver.switch_to.alert
    alert_text = alert.text
    assert alert_text == "This is an alert box!"
    alert.accept()

    # Нажимаем на вторую кнопку (Confirm)
    confirm_button = driver.find_element(By.CSS_SELECTOR, "button:nth-child(2)")
    confirm_button.click()

    # Отклоняем Confirm
    confirm = driver.switch_to.alert
    confirm_text = confirm.text
    assert confirm_text == "Do you want to continue?"
    confirm.dismiss()

    # Нажимаем на третью кнопку (Prompt)
    prompt_button = driver.find_element(By.CSS_SELECTOR, "button:nth-child(3)")
    prompt_button.click()

    # Вводим значение в Prompt
    prompt = driver.switch_to.alert
    prompt.send_keys("42")
    prompt_text = prompt.text
    assert prompt_text == "What is 5 + 5?"
    prompt.accept()

    # Проверяем текст на странице
    result_text = driver.find_element(By.CSS_SELECTOR, "#result").text
    assert result_text == "Correct!"
finally:
# Ждем 5 секунд, затем закрываем браузер
    time.sleep(5)
    driver.quit()
