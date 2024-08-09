from selenium import webdriver

from selenium.webdriver.common.by import By

import time
try:
    driver = webdriver.Chrome()

    driver.get('https://erikdark.github.io/Qa_autotest_03/')
    time.sleep(0.15)
    element=driver.find_element(By.CSS_SELECTOR,'#email').send_keys('77777@mail.yes')
    time.sleep(0.15)
    element=driver.find_element(By.CSS_SELECTOR,'#firstName').send_keys('Nama')
    time.sleep(0.15)
    element=driver.find_element(By.CSS_SELECTOR,'#lastName').send_keys('Namanama')
    time.sleep(0.15)
    element=driver.find_element(By.TAG_NAME,'button').click()
    time.sleep(3)
finally:

    driver.quit()