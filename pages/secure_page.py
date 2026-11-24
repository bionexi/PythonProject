from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

success_selector = (By.CSS_SELECTOR, ".flash.success")
class SecurePage(LoginPage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://the-internet.herokuapp.com/secure')

    def get_success_text(self):
        return self.wait.until(EC.visibility_of_element_located(success_selector)).text