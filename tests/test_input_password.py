from pages.login_page import LoginPage

def test_input_password(browser):
    login_page = LoginPage(browser)
    login_page.open()
    assert login_page.password_is_displayed()

def test_password_is_entered(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.enter_password_value("SuperSecretPassword!")
    assert login_page.get_password_field_type() == "SuperSecretPassword!"