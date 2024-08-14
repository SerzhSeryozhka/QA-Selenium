from selenium import webdriver

from selenium.webdriver.common.by import By

import time
try:
    driver = webdriver.Chrome()

    driver.get('https://erikdark.github.io/QA_autotests_13/')
    print('Стр загрузилась')
    button = driver.find_element(By.ID, 'openNewPageBtn').click()
    print('Кнпк1 нажата')
    new_tab = driver.window_handles[1]
    print('Найдено новое окно')
    driver.switch_to.window(new_tab)
    print('Перейдено в новое окно')
    button1 = driver.find_element(By. ID, 'displayTextBtn').click()
    print('Кнп2 нажата')
    disp_txt = driver.find_element(By.ID,'displayText').text
    print('Текст получен')
    assert disp_txt == 'Я СДЕЛАЛ',f'Текст не совпадает: ожидалось Я СДЕЛАЛ, но было {disp_txt}'
    print('Текст == ',disp_txt)
finally:
    time.sleep(3)
    driver.quit()
    print('Конец')