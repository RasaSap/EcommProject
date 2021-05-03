from POMProject.Pages.address import AddressPage
from POMProject.Pages.cartModal import CartModal
from POMProject.Pages.homePage import HomePage
from POMProject.Pages.productList import ProductListPage
from POMProject.Pages.payment import PaymentPage
from POMProject.Pages.productDetails import ProductDetailsPage
from POMProject.Pages.shipping import ShippingPage
from POMProject.Pages.signInPage import SignInPage
from POMProject.Pages.cartSummary import CartSummaryPage

from selenium import webdriver
import HTMLTestRunner
import unittest
import time


class Test01(unittest.TestCase):

    def setUpClass(self):
        self.driver = webdriver.Chrome(
            executable_path=r'C:\Users\oska\PycharmProjects\EcommProject\drivers\chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://automationpractice.com/index.php")

    def test_page_loads(self):
        self.driver = self.driver

        homepage = HomePage(self.driver)
        self.assertTrue(homepage.is_header_logo_present())

    def test_sign_in_valid(self):
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_sign_in()

        sign_in = SignInPage(driver)
        sign_in.enter_email("rasa.saproniene@gmail.com")
        sign_in.enter_password("Oskaras12")
        sign_in.click_sign_in()

        self.assertEqual(homepage.get_user_name_in_header(), "Rasa Sap", "User name assert failed")

    def test_shopping(self):
        driver = self.driver

        homepage = HomePage(driver)
        homepage.search_category('dress')

        item_list = ProductListPage(driver)
        time.sleep(2)
        item_list.click_first_product()

        product_details = ProductDetailsPage(driver)
        product_details.click_add_to_cart_button()

        cart_modal = CartModal(driver)
        cart_modal.click_proceed_to_checkout()

        summary = CartSummaryPage(driver)
        summary.click_proceed_to_checkout()

        sign_in = SignInPage(driver)
        sign_in.enter_email("rasa.saproniene@gmail.com")
        sign_in.enter_password("Oskaras12")
        sign_in.click_sign_in()

        address = AddressPage(driver)
        address.click_proceed_to_checkout()

        shipping = ShippingPage(driver)
        shipping.click_terms_of_service_checkbox()
        shipping.click_proceed_to_checkout()

        payment = PaymentPage(driver)
        payment.click_pay_by_bank()
        payment.click_confirm_order()

        unittest.TestCase().assertEqual(payment.get_order_confirmation_message(), "Your order on My Store is complete.",
                                        "Order was not completed")

    def test_homepage(self):
        driver = self.driver

        homepage = HomePage(driver)

        self.assertTrue(homepage.are_links_in_slider_row_valid())
        self.assertTrue(homepage.is_slider_arrow_next_enabled())
        self.assertTrue(homepage.is_slider_arrow_previous_enabled())
        self.assertTrue(len(homepage.best_sellers_products()) > 0, "Best sellers products are not displayed")
        self.assertTrue(len(homepage.popular_products()) > 0, "Popular products are not displayed")

    def test_product_list(self):
        driver = self.driver

        homepage = HomePage(driver)
        homepage.search_category('dress')

        item_list = ProductListPage(driver)
        product_number_by_grid = item_list.get_product_no_in_grid()
        product_number_by_list = item_list.get_product_no_in_list()

        unittest.TestCase().assertEqual(product_number_by_grid, product_number_by_list,
                                        "defect: product no is not equal in list and grid ")

        unittest.TestCase().assertEqual(item_list.get_sort_options_number(), 8,
                                        "defect: not 8 options in sort dropdown")

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

    def tearDownClass(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/oska/PycharmProjects/EcommProject/reports'))
