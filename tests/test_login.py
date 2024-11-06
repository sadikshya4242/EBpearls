import time

import pytest
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_valid_login(self):
       login_page = LoginPage(self.driver)
       login_page.login("Sadikshya00","1234")
       assert "Accounts Overview" in self.driver.title
       time.sleep(2)
       login_page.logout()
       time.sleep(2)

    def test_empty_username(self):
        login_page = LoginPage(self.driver)
        login_page.login("", "password123")
        error_message = login_page.get_error_message()
        time.sleep(2)
        assert "Please enter a username and password" in error_message
        time.sleep(2)

    def test_empty_password(self):
        login_page = LoginPage(self.driver)
        login_page.login("validUsername", "")
        error_message = login_page.get_error_message()
        time.sleep(2)
        assert "Please enter a username and password" in error_message
        time.sleep(2)
    def test_invalid_login(self):
        login_page = LoginPage(self.driver)
        login_page.login("name", "Password")
        error_message = login_page.get_error_message()
        assert "The username and password could not be verified." in error_message
        time.sleep(2)
