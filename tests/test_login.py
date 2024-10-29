import time

import pytest
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_valid_login(self):
       login_page = LoginPage(self.driver)
       login_page.login("hello_user_7_1","password123")
       assert "Accounts Overview" in self.driver.title
    def test_empty_username(self):
        login_page = LoginPage(self.driver)
        login_page.login("", "password123")
        error_message = login_page.get_error_message()
        time.sleep(2)
        assert "Please enter a username" in error_message
        time.sleep(2)
    def test_empty_password(self):
        login_page = LoginPage(self.driver)
        login_page.login("validUsername", "")
        error_message = login_page.get_error_message()
        time.sleep(2)
        assert "Please enter a password" in error_message
        time.sleep(2)
    def test_invalid_login(self):
        login_page = LoginPage(self.driver)
        login_page.login("name", "Password")

        try:
            error_message = self.driver.find_element(By.XPATH, "//span[contains(text(), 'The username and password could not be verified.')]").text
            assert "The username and password could not be verified." in error_message, "Error message not displayed as expected."
        except:
            assert False, "Login succeeded with invalid credentials or error message was not found."

        time.sleep(2)
