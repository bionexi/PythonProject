from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


button_selector = (By.CLASS_NAME, "radius")
username_selector = (By.ID, 'username')
password_selector = (By.ID, "password")
error_selector = (By.CSS_SELECTOR, ".flash.error")

logout_selector = (By.CSS_SELECTOR, ".button.secondary.radius")

class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://the-internet.herokuapp.com/login')

    def button(self):
        return self.find(button_selector)

    def username(self):
        return self.find(username_selector)

    def password(self):
        return self.find(password_selector)

    def button_is_displayed(self):
        return self.button().is_displayed()

    def button_click(self):
        self.button().click()

    def username_is_displayed(self):
        return self.username().is_displayed()

    def password_is_displayed(self):
        return self.password().is_displayed()

    def enter_full_name(self, name):
        field = self.wait.until(EC.visibility_of_element_located(username_selector))
        field.clear()
        field.send_keys(name)

    def get_full_name_value(self):
        field = self.wait.until(EC.visibility_of_element_located(username_selector))
        return field.get_attribute("value")

    def enter_password_value(self, password):
        field = self.wait.until(EC.visibility_of_element_located(password_selector))
        field.clear()
        field.send_keys(password)

    def get_password_field_type(self):
        field = self.wait.until(EC.visibility_of_element_located(password_selector))
        return field.get_attribute("value")

    def get_error_text(self):
        return self.wait.until(EC.visibility_of_element_located(error_selector)).text