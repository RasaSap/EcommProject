from POMProject.Pages.homePage import HomePage
from POMProject.Utils.MainTest import MainTest


class HomepageTest(MainTest):

    def test_homepage(self):
        driver = self.driver

        homepage = HomePage(driver)

        self.assertTrue(homepage.are_links_in_slider_row_valid())
        self.assertTrue(homepage.is_slider_arrow_next_enabled())
        self.assertTrue(homepage.is_slider_arrow_previous_enabled())
        self.assertTrue(len(homepage.best_sellers_products()) > 0, "Best sellers products are not displayed")
        self.assertTrue(len(homepage.popular_products()) > 0, "Popular products are not displayed")
