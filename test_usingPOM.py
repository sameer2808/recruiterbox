import pytest

from recruiterbox.ApplyJob import ApplyJob
from recruiterbox.HomePage import HomePage


@pytest.mark.usefixtures("init_driver")
class TestLogin:

    """   Perform action to search job position having title Fullstack """
    def test_input(self):
        self.homePage = HomePage(self.driver)
        self.homePage.do_searchposition(self.homePage.search_textbox,'Fullstack')

    """   Perform action to click on the first job position having title Fullstack """

    def test_selectjob(self):
        self.homePage = HomePage(self.driver)
        self.homePage.do_selectposition()

    """   Perform action to Apply, Submit and then assert the confirmation message  """

    def test_applyjob(self):
        self.applyjob = ApplyJob(self.driver)
        self.applyjob.do_clickApply()
        self.applyjob.do_clickSubmit()
        assert "Your application has been submitted successfully!", self.applyjob.do_getconfirmtxt()