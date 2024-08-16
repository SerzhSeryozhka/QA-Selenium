import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
"""
 КЛАСС ВСЕГДА С БОЛЬШОЙ БУКВЫ ИНАЧЕ ОН NULL
"""
class TestwebPage:
    @pytest.fixture
    def driver(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://erikdark.github.io/Qa_autotests_reg_form_pop_up/')
        yield self.driver
        self.driver.quit()

    def test_valid_login_close_modal(self, driver):
        driver.find_element(By.ID,'openModalButton').click()

        driver.find_element(By.ID,'username').send_keys('testuser')
        driver.find_element(By.ID,'password').send_keys('password123')
        driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()

        modal = driver.find_element(By.ID,'loginModal')
        WebDriverWait(driver,10).until(EC.invisibility_of_element(modal))
        assert not  modal.is_displayed(),'модалка должна быть закрыта'

    def test_invalid_login_close_modal(self, driver):
        driver.find_element(By.ID,'openModalButton').click()

        driver.find_element(By.ID,'username').send_keys('testuser1')
        driver.find_element(By.ID,'password').send_keys('password123')
        driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()

        alert = WebDriverWait(driver,10).until(EC.alert_is_present())

        assert alert.text == 'Invalid username or password','text в алерт будет таким'
        alert.accept()

        modal = driver.find_element(By.ID,'loginModal')
        assert  modal.is_displayed(),'модалка должна быть закрыта'