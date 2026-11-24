from pages.login_page import LoginPage

def test_input_username(browser):
    login_page = LoginPage(browser)
    login_page.open()
    assert login_page.username_is_displayed()

def test_full_name_is_entered(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.enter_full_name("Иван Иванов")

    assert login_page.get_full_name_value() == "Иван Иванов"