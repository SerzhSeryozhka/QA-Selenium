    #Импортруруем набор команд для управления браузером
from selenium import webdriver
    #импортируем класс By, который позволяет выбрать способ поиска элемента на странице
from selenium.webdriver.common.by import By
    #импорт билбиотеки время
import time
    #инцииилизация драйвера
try:
    driver = webdriver.Chrome()

    driver.get('https://erikdark.github.io/hide-button-blocked-button-/')
    butt_cl = driver.find_element(By.CSS_SELECTOR, "button")
    for b in butt_cl:
        butt_cl.click()
        time.sleep(0.5)
finally:
    time.sleep(3)
#ЗАКРЫВАЕТСЯ
    driver.quit()
