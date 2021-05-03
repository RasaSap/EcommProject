from POMProject.Pages.cartModal import CartModal
from POMProject.Pages.cartSummary import CartSummaryPage
from POMProject.Pages.homePage import HomePage
from POMProject.Pages.productDetails import ProductDetailsPage
from POMProject.Pages.productList import ProductListPage
from POMProject.Utils.MainTest import MainTest
import time


class CartSummaryTest(MainTest):

    def test_cart_summary(self):
        driver = self.driver

        homepage = HomePage(driver)
        product_list = ProductListPage(driver)
        product_details = ProductDetailsPage(driver)
        cart_modal = CartModal(driver)
        cart_summary = CartSummaryPage(driver)

        homepage.search_category('blouse')
        time.sleep(2)
        product_list.click_first_product()
        product_details.click_add_to_cart_button()
        cart_modal.click_continue_shopping()

        homepage.search_category('top')
        time.sleep(2)
        product_list.click_first_product()
        product_details.click_add_to_cart_button()
        cart_modal.click_proceed_to_checkout()
        cart_summary.delete_first_product()
        cart_summary.click_continue_shopping()

        homepage.search_category('top')
        time.sleep(2)
        product_list.click_first_product()
        product_details.click_add_to_cart_button()
        cart_modal.click_proceed_to_checkout()
        self.assertEqual(cart_summary.get_quantity(), "2", "Quantity does not match")
