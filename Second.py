from selenium import webdriver

from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()

driver.get('https://erikdark.github.io/Qa_autotest_02/')
element=driver.find_element(By.ID,'phone').send_keys('+77777777777')
element=driver.find_element(By.ID,'email').send_keys('77777@mail.yes')
element=driver.find_element(By.ID,'name').send_keys('Nama')
element=driver.find_element(By.ID,'password').send_keys('****4****')
element=driver.find_element(By.ID,'submitBtn').click()
time.sleep(10)
driver.quit()