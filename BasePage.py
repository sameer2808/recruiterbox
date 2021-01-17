from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


""" Base Class for creating the common methods to be shared across Page class """

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    """ Click method to be invoked from Page class taking locator as an argument """
    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    """ Send_keys method to be invoked from Page class taking locator as an argument """
    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    """ Get text  method to be invoked from Page class taking locator as an argument """
    def do_get_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text
