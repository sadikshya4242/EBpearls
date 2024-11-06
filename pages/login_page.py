import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_input = (By.XPATH, "//input[@name='username']")
        self.password_input = (By.XPATH, "//input[@name='password']")
        self.login_button = (By.XPATH, "//input[@value='Log In']")
        self.error_message = (By.XPATH, "//p[@class='error']")
        self.logout_button=(By.XPATH,"//a[.='Log Out']")

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.username_input)
        )
        self.enter_text(self.username_input, username)
        self.enter_text(self.password_input, password)
        self.click(self.login_button)

    def logout(self):
        time.sleep(2)
        self.click(self.logout_button)
    def get_error_message(self):
        # Retrieve the error message displayed on login failure
        return self.get_text(self.error_message)
