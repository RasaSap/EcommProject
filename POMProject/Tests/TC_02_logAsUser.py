from POMProject.Pages.signInPage import SignInPage
from POMProject.Pages.homePage import HomePage
from POMProject.Utils.MainTest import MainTest


class SignInTest(MainTest):

    def test_sign_in_valid(self):
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_sign_in()

        sign_in = SignInPage(driver)
        sign_in.enter_email("rasa.saproniene@gmail.com")
        sign_in.enter_password("Oskaras12")
        sign_in.click_sign_in()

        self.assertEqual(homepage.get_user_name_in_header(), "Rasa Sap", "User name assert failed")
