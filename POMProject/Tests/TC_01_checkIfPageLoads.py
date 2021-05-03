from POMProject.Pages.homePage import HomePage
from POMProject.Utils.MainTest import MainTest


class Test01(MainTest):

    def test_page_loads(self):
        driver = self.driver

        homepage = HomePage(driver)
        self.assertTrue(homepage.is_header_logo_present())
