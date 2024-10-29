from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.register_link = (By.XPATH, "//a[text()='Register']")
        self.first_name_input = (By.ID, "customer.firstName")
        self.last_name_input = (By.ID, "customer.lastName")
        self.address_input = (By.ID, "customer.address.street")
        self.city_input = (By.ID, "customer.address.city")
        self.state_input = (By.ID, "customer.address.state")
        self.zip_code_input = (By.ID, "customer.address.zipCode")
        self.phone_input = (By.ID, "customer.phoneNumber")
        self.ssn_input = (By.ID, "customer.ssn")
        self.username_input = (By.ID, "customer.username")
        self.password_input = (By.ID, "customer.password")
        self.confirm_password_input = (By.ID, "repeatedPassword")
        self.register_button = (By.XPATH, "//input[@value='Register']")

    def register(self, first_name, last_name, address, city, state, zip_code, phone, ssn, base_username, password):
        # Click the register link
        self.click(self.register_link)

        # Fill in the registration form
        self.enter_text(self.first_name_input, first_name)
        self.enter_text(self.last_name_input, last_name)
        self.enter_text(self.address_input, address)
        self.enter_text(self.city_input, city)
        self.enter_text(self.state_input, state)
        self.enter_text(self.zip_code_input, zip_code)
        self.enter_text(self.phone_input, phone)
        self.enter_text(self.ssn_input, ssn)

        # Create a unique username
        unique_username = f"{base_username}_{self.get_username_counter()}"
        self.enter_text(self.username_input, unique_username)

        self.enter_text(self.password_input, password)
        self.enter_text(self.confirm_password_input, password)

        # Click the register button
        self.click(self.register_button)

        return unique_username

    def get_username_counter(self):
        # Implement a simple counter here or fetch from a file for persistence
        return 1  # Replace with actual counter logic
