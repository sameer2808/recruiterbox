from selenium.webdriver.common.by import By

from recruiterbox.BasePage import BasePage


class ApplyJob(BasePage):

    apply_btn = (By.XPATH, '//a[contains(text(), "Apply")]')
    submit_btn = (By.ID, 'input_application_form_submit')
    txt_msg = (By.XPATH, '//div/div/p[@class="meta-app-success-message"]')

    def do_clickApply(self):
        self.do_click(self.apply_btn)

    def do_clickSubmit(self):
        self.do_click(self.submit_btn)

    def do_getconfirmtxt(self):
        self.do_get_text(self.txt_msg)