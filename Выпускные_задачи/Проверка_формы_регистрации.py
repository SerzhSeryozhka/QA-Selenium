import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestWebPage:
    @pytest.fixture(scope='module')
    def browser():
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        yield driver
        driver.quit()
    @pytest.fixture
    def open_form(browser):
        browser.get('https://erikdark.github.io/QA_DIPLOM/registration.html')
        yield
        browser.refresh()


    # Валидные данные
    def test_valid_password(browser,open_form):
      time.sleep(2)
      name_input = browser.find_element(By.ID,'name')
      name_input.send_keys('Серж')
      email_input = browser.find_element(By.ID,'email')
      email_input.send_keys('example@example.ru')
      pw_input = browser.find_element(By.ID,'password')
      pw_input.send_keys('Password123')
      pw_input = browser.find_element(By.ID,'confirmPassword')
      pw_input.send_keys('Password123')
      btn = browser.find_element(By.CSS_SELECTOR,'button[type="submit"]')
      btn.click()
      message = browser.find_element(By.ID,'message').text
      assert message == 'Регистрация успешна!'

    # # Короткий парроль
    # def test_invalid_short_password(browser,open_form):
    #   name_input = browser.find_element(By.ID,'name')
    #   name_input.send_keys('Серж')
    #   email_input = browser.find_element(By.ID,'email')
    #   email_input.send_keys('example@example.ru')
    #   pw_input = browser.find_element(By.ID,'password')
    #   pw_input.send_keys('Pass123')
    #   pw_input = browser.find_element(By.ID,'confirmPassword')
    #   pw_input.send_keys('Pass123')
    #   btn = browser.find_element(By.CSS_SELECTOR,'button[type="submit"]')
    #   btn.click()
    #   message = browser.find_element(By.ID,'message').text
    #   assert message == 'Пароль должен содержать не менее 8 символов, включая 1 заглавную букву, 1 строчную букву и 1 цифру'

    # # Все символы пароля в нижнем регистре
    # def test_invalid_no_upper_password(browser,open_form):
    #   name_input = browser.find_element(By.ID,'name')
    #   name_input.send_keys('Серж')
    #   email_input = browser.find_element(By.ID,'email')
    #   email_input.send_keys('example@example.ru')
    #   pw_input = browser.find_element(By.ID,'password')
    #   pw_input.send_keys('password123')
    #   pw_input = browser.find_element(By.ID,'confirmPassword')
    #   pw_input.send_keys('password123')
    #   btn = browser.find_element(By.CSS_SELECTOR,'button[type="submit"]')
    #   btn.click()
    #   message = browser.find_element(By.ID,'message').text
    #   assert message == 'Пароль должен содержать не менее 8 символов, включая 1 заглавную букву, 1 строчную букву и 1 цифру'


    # # Все символы пароля в верхнем регистре
    # def test_invalid_no_lower_password(browser,open_form):
    #   name_input = browser.find_element(By.ID,'name')
    #   name_input.send_keys('Серж')
    #   email_input = browser.find_element(By.ID,'email')
    #   email_input.send_keys('example@example.ru')
    #   pw_input = browser.find_element(By.ID,'password')
    #   pw_input.send_keys('PASSWORD123')
    #   pw_input = browser.find_element(By.ID,'confirmPassword')
    #   pw_input.send_keys('PASSWORD123')
    #   btn = browser.find_element(By.CSS_SELECTOR,'button[type="submit"]')
    #   btn.click()
    #   message = browser.find_element(By.ID,'message').text
    #   assert message == 'Пароль должен содержать не менее 8 символов, включая 1 заглавную букву, 1 строчную букву и 1 цифру'


    # # Пароль без цифр
    # def test_invalid_no_digit_password(browser,open_form):
    #   name_input = browser.find_element(By.ID,'name')
    #   name_input.send_keys('Серж')
    #   email_input = browser.find_element(By.ID,'email')
    #   email_input.send_keys('example@example.ru')
    #   pw_input = browser.find_element(By.ID,'password')
    #   pw_input.send_keys('PASSWORDDDD')
    #   pw_input = browser.find_element(By.ID,'confirmPassword')
    #   pw_input.send_keys('PASSWORDDDD')
    #   btn = browser.find_element(By.CSS_SELECTOR,'button[type="submit"]')
    #   btn.click()
    #   message = browser.find_element(By.ID,'message').text
    #   assert message == 'Пароль должен содержать не менее 8 символов, включая 1 заглавную букву, 1 строчную букву и 1 цифру'



    # def test_invalid_missing_password(browser,open_form):
    #   name_input = browser.find_element(By.ID,'name')
    #   name_input.send_keys('Серж')
    #   email_input = browser.find_element(By.ID,'email')
    #   email_input.send_keys('example@example.ru')
    #   pw_input = browser.find_element(By.ID,'password')
    #   pw_input.send_keys('')
    #   pw_input = browser.find_element(By.ID,'confirmPassword')
    #   pw_input.send_keys('PASSWORDDDD')
    #   btn = browser.find_element(By.CSS_SELECTOR,'button[type="submit"]')
    #   btn.click()
    #   message = browser.find_element(By.ID,'message').text
    #   actual_message = email_input.get_attribute('validationMessage')
    #   assert  actual_message == actual_message

    # def test_invalid_missing_password(browser,open_form):
    #   name_input = browser.find_element(By.ID,'name')
    #   name_input.send_keys('Серж')
    #   email_input = browser.find_element(By.ID,'email')
    #   email_input.send_keys('example@example.ru')
    #   pw_input = browser.find_element(By.ID,'password')
    #   pw_input.send_keys('')
    #   pw_input = browser.find_element(By.ID,'confirmPassword')
    #   pw_input.send_keys('PASSWORDDDD')
    #   btn = browser.find_element(By.CSS_SELECTOR,'button[type="submit"]')
    #   btn.click()
    #   message = browser.find_element(By.ID,'message').text
    #   actual_message = email_input.get_attribute('validationMessage')
    #   assert  actual_message == actual_message




    # def test_valid_Confirmpassword(browser,open_form):

    #   name_input = browser.find_element(By.ID,'name')
    #   name_input.send_keys('Серж')
    #   email_input = browser.find_element(By.ID,'email')
    #   email_input.send_keys('example@example.ru')
    #   pw_input = browser.find_element(By.ID,'password')
    #   pw_input.send_keys('Password123')
    #   pw_input = browser.find_element(By.ID,'confirmPassword')
    #   pw_input.send_keys('Password123')
    #   btn = browser.find_element(By.CSS_SELECTOR,'button[type="submit"]')
    #   btn.click()
    #   message = browser.find_element(By.ID,'message').text
    #   assert message == 'Регистрация успешна!'


    # def test_invalid_Confirmpassword(browser,open_form):
    #   name_input = browser.find_element(By.ID,'name')
    #   name_input.send_keys('Серж')
    #   email_input = browser.find_element(By.ID,'email')
    #   email_input.send_keys('example@example.ru')
    #   pw_input = browser.find_element(By.ID,'password')
    #   pw_input.send_keys('Password123')
    #   pw_input = browser.find_element(By.ID,'confirmPassword')
    #   pw_input.send_keys('Password1234')
    #   btn = browser.find_element(By.CSS_SELECTOR,'button[type="submit"]')
    #   btn.click()
    #   message = browser.find_element(By.ID,'message').text
    #   assert message == 'Пароли не совпадают'


    #   # Пароли не совпадают
    # def test_invalid_Confirmpassword(browser,open_form):
    #   name_input = browser.find_element(By.ID,'name')
    #   name_input.send_keys('Серж')
    #   email_input = browser.find_element(By.ID,'email')
    #   email_input.send_keys('example@example.ru')
    #   pw_input = browser.find_element(By.ID,'password')
    #   pw_input.send_keys('Password123')
    #   pw_input = browser.find_element(By.ID,'confirmPassword')
    #   pw_input.send_keys('')
    #   btn = browser.find_element(By.CSS_SELECTOR,'button[type="submit"]')
    #   btn.click()
    #   message = browser.find_element(By.ID,'message').text
    #   actual_message = email_input.get_attribute('validationMessage')
    #   assert  actual_message == actual_message   