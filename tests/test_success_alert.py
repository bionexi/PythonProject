from pages.secure_page import SecurePage
from pages.login_page import LoginPage

def test_success_login(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.enter_full_name("tomsmith")
    login_page.enter_password_value("SuperSecretPassword!")
    login_page.button_click()

    secure_page = SecurePage(browser)
    assert "You logged into a secure area!" in secure_page.get_success_text()