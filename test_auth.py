import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://azs.tatneft.ru/"


@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Chrome(executable_path="./chromedriver")
    yield browser
    browser.quit()


class TestAuthorization:
    def test_auth_user(self, browser):
        browser.get(link)
        input_name = browser.find_element(By.NAME, 'login')
        input_password = browser.find_element(By.NAME, 'password')
        login_button = browser.find_element(By.CLASS_NAME, '.btn-new__content')

        input_name.send_keys("log")
        input_password.send_keys("pass")
        login_button.click()
        login = browser.find_element(By.XPATH, '/html/body/header/name').text
        assert login == 'log'
