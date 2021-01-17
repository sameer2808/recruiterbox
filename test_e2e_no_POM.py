import time

from selenium import webdriver
from selenium.webdriver import ActionChains


""" Below test performs the following steps         """
"""     1. Launch the app                           """
"""     2. Search for FullStack engineer position   """
"""     3. Apply for Fullstack job position         """
"""     4. Submit the application                   """
"""     5. Perform assert on the final confirmation message on applying successfully  """


def test_e2e():
    driver = webdriver.Chrome(executable_path="D://Python/chromedriver.exe")

    """ Launching the app """
    driver.get("https://sdetapplication.recruiterbox.com/")
    driver.maximize_window()

    """ Searching job positions having title FullStack """
    driver.find_element_by_name('q').send_keys("Fullstack")
    time.sleep(3)

    #driver.find_elements_by_xpath("//button[@class='rb-input__button']")

    """ Using ActionsChains class to click on the search button as it not getting recognized by find elements method"""
    action = ActionChains(driver)
    menu = driver.find_element_by_xpath("//button[@class='rb-input__button']")
    action.move_to_element(menu).click().perform()

    """ Clicking on the first Fullstack job position from search results """
    driver.find_element_by_xpath("//h3[contains(text(), '                    Fullstack Engineer')]").click()

    """ Clicking on Apply button """
    driver.find_element_by_xpath("//a[contains(text(), 'Apply')]").click()
    time.sleep(2)

    """ Clicking on Submit button """
    driver.find_element_by_id("input_application_form_submit").click()
    time.sleep(2)

    """ Performing an assert on the final confirmation text on the confirmation page """
    msg = driver.find_element_by_xpath("//div/div/p[@class='meta-app-success-message']").text
    assert "Your application has been submitted successfully!", msg