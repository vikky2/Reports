from selenium import webdriver
import pytest

class TestOrangeHRM():

    @pytest.fixture()
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_homepageTitle(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        assert self.driver.title=="OrangeHRM"

    def test_login(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()

        assert self.driver.title=="OrangeHRM"

        #html report generated in the pycharm folder---------- generated html file: file://C:\Users\D\PycharmProjects\Reports\report.html ------------






