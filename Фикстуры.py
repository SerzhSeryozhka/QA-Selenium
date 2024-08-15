import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'https://selenium1py.pythonanywhere.com/ru/'




@pytest.fixture
def driver():
    print('\n start browser for test...')
    driver = webdriver.Chrome()
    yield driver
    #этот код выполнится полсе теста
    print('\nquit browser')
    driver.quit()
