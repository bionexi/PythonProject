from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def find(self, locator):
        return self.browser.find_element(*locator)

    