from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Создание экземпляра драйвера Chrome
driver = webdriver.Chrome()

# Переход на страницу с формой
driver.get("https://erikdark.github.io/QA_DIPLOM_X2/first_test_capcha.html")

# Заполнение формы
nama = "Кудрявцев С.А."
driver.find_element(By.ID, "name").send_keys(nama)
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

# Ожидание появления captcha-контейнера
wait = WebDriverWait(driver, 10)
captcha_container = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "captcha-container")))

captcha_images = captcha_container.find_elements(By.TAG_NAME, "img")

# Цикл, который кликает по captcha-изображениям, пока не будет найдена правильная
i=0
while i <len(captcha_images):

    random_image = captcha_images[i]  # Выбираем первую картинку

    random_image.click()
    i+=1

    # Ожидание появления сообщения об успешном прохождении captcha
    alert = wait.until(EC.alert_is_present())
    alert_text = alert.text
    if nama in alert_text:
    
        break
    else:
        # Если фамилия не найдена в сообщении, нажимаем на алерт и выбираем следующее captcha-изображение
    
        alert.accept()
        captcha_images = captcha_container.find_elements(By.TAG_NAME, "img")
        continue


assert "Кудрявцев С.А." in alert_text
print(f"Фамилия присутствует в сообщении! = {alert_text}")

# Закрытие браузера
driver.quit()