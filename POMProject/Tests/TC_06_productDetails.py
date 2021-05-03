from POMProject.Pages.cartModal import CartModal
from POMProject.Pages.cartSummary import CartSummaryPage
from POMProject.Pages.homePage import HomePage
from POMProject.Pages.productDetails import ProductDetailsPage
from POMProject.Pages.productList import ProductListPage
from POMProject.Utils.MainTest import MainTest
import time


class ProductDetailsTest(MainTest):

    def test_product_details(self):
        driver = self.driver

        homepage = HomePage(driver)
        homepage.search_category('dress')

        item_list = ProductListPage(driver)
        time.sleep(2)
        item_list.click_first_product()

        product_details = ProductDetailsPage(driver)
        product_details.click_view_larger_img()
        product_details.click_close_img()
        one_item_price = float(product_details.get_product_price())

        product_details.click_quantity_up()
        product_details.choose_size("M")
        product_details.click_add_to_cart_button()

        cart_modal = CartModal(driver)
        cart_modal.click_proceed_to_checkout()

        cart_summary = CartSummaryPage(driver)
        cart_summary.total_product_price()
        total_price_from_cart = float(cart_summary.total_product_price())
        total_price = one_item_price * 2
        self.assertEqual(total_price_from_cart, total_price, "Total price does not match")
        self.assertEqual(cart_summary.product_size(), "M", "Size does match")
