import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.registration_page import RegistrationPage

@pytest.mark.usefixtures("setup")
class TestRegistration:

    def test_valid_registration_newusername(self):
        registration_page = RegistrationPage(self.driver)
        base_username = "hello_user_7"  # Base username to be incremented
        username = registration_page.register(
            "sadikshya", "bhusal", "baneshwor", "kathmandu", "bagmati",
            "12345", "1234567890", "123-45-6789", base_username, "password123"
        )

        try:
            success_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Your account was created successfully')]"))
            ).text
            assert "Your account was created successfully" in success_message
            print(f"Registered with username: {username}")
        except Exception as e:
            print(f"Error occurred: {e}")
            assert False, "Expected success message not displayed."

    def test_empty_fields(self):
        registration_page = RegistrationPage(self.driver)
        registration_page.click(registration_page.register_link)
        registration_page.click(registration_page.register_button)
        time.sleep(2)
        first_name_error = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='First name is required.']"))
        )
        assert first_name_error.is_displayed(), "Expected 'First name is required.' error message is not displayed."
        assert first_name_error.text == "First name is required.", "Error message text does not match the expected value."

    def test_registration_with_existing_username(self):
        registration_page = RegistrationPage(self.driver)
        registration_page.register(
            "sadikshya", "bhusal", "baneshwor", "kathmandu", "bagmati",
            "12345", "1234567890", "123-45-6789", "hello_user_4_1", "password123"
        )
        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'This username already exists')]"))
        ).text
        assert "This username already exists" in error_message, "Expected 'This username already exists' error message not displayed."
