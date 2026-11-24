from pages.login_page import LoginPage

def test_button_login(browser):
    login_page = LoginPage(browser)
    login_page.open()
    assert login_page.button_is_displayed()

def test_button_click(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.button_click()
    assert "Your username is invalid!" in login_page.get_error_text()
