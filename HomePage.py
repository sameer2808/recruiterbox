from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from recruiterbox.BasePage import BasePage


class HomePage(BasePage):
    search_textbox = (By.NAME, 'q')
    #search_btn = (By.XPATH, '//button[@class="rb-input__button"]')
    menu = (By.XPATH, '//button[@class="rb-input__button"]')
    search_results = (By.XPATH, '//h3[contains(text(), "                    Fullstack Engineer")]')

    """  Constructor of the page class  """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://sdetapplication.recruiterbox.com/")

    """   Page Actions                """
    """-------------------------------"""


    """   Method to search a Job position with the title Fullstack """
    def do_searchposition(self, search_textbox, searchtxt):
        self.do_send_keys(self.search_textbox, searchtxt)
        #self.do_click()
        action = ActionChains(self.driver)
        search_btn = self.driver.find_element_by_xpath("//button[@class='rb-input__button']")
        action.move_to_element(search_btn).click().perform()

    """   Method to Click on the FullStack engineer job position from the job results retrieved """
    def do_selectposition(self):
        self.do_click(self.search_results)



