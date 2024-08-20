import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestWebPage:
    @pytest.fixture(scope='module')
    def driver(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://example.com/register")
        yield self.driver
        self.driver.quit()

    def test_validate_name(self, driver):
        # Проверка валидного имени
        self.enter_valid_registration_data(driver)
        assert "Thank you for registering" in driver.page_source

        # Проверка невалидного имени
        self.enter_invalid_name(driver)
        assert "Please enter a valid name" in driver.page_source

    def test_validate_email(self, driver):
        # Проверка валидного email-адреса
        self.enter_valid_registration_data(driver)
        assert "Thank you for registering" in driver.page_source

        # Проверка невалидного email-адреса
        self.enter_invalid_email(driver)
        assert "Please enter a valid email address" in driver.page_source

    def test_validate_password(self, driver):
        # Проверка валидного пароля
        self.enter_valid_registration_data(driver)
        assert "Thank you for registering" in driver.page_source

        # Проверка невалидного пароля
        self.enter_invalid_password(driver)
        assert "Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one digit" in driver.page_source

    def test_validate_password_confirmation(self, driver):
        # Проверка совпадающего пароля и подтверждения
        self.enter_valid_registration_data(driver)
        assert "Thank you for registering" in driver.page_source

        # Проверка несовпадающего пароля и подтверждения
        self.enter_mismatching_passwords(driver)
        assert "Passwords do not match" in driver.page_source

    def enter_valid_registration_data(self, driver):
        driver.find_element(By.ID, "name").send_keys("Serzh")
        driver.find_element(By.ID, "email").send_keys("serzh@example.com")
        driver.find_element(By.ID, "password").send_keys("Passw0rd")
        driver.find_element(By.ID, "confirm_password").send_keys("Passw0rd")
        driver.find_element(By.ID, "submit").click()

    def enter_invalid_name(self, driver):
        driver.find_element(By.ID, "name").clear()
        driver.find_element(By.ID, "name").send_keys("John Doe")
        driver.find_element(By.ID, "email").send_keys("johndoe@example.com")
        driver.find_element(By.ID, "password").send_keys("Passw0rd")
        driver.find_element(By.ID, "confirm_password").send_keys("Passw0rd")
        driver.find_element(By.ID, "submit").click()

    def enter_invalid_email(self, driver):
        driver.find_element(By.ID, "email").clear()
        driver.find_element(By.ID, "email").send_keys("johndoe@")
        driver.find_element(By.ID, "password").send_keys("Passw0rd")
        driver.find_element(By.ID, "confirm_password").send_keys("Passw0rd")
        driver.find_element(By.ID, "submit").click()

    def enter_invalid_password(self, driver):
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "password").send_keys("password")
        driver.find_element(By.ID, "confirm_password").send_keys("password")
        driver.find_element(By.ID, "submit").click()

    def enter_mismatching_passwords(self, driver):
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "password").send_keys("Passw0rd")
        driver.find_element(By.ID, "confirm_password").send_keys("passw0rd")
        driver.find_element(By.ID, "submit").click()
