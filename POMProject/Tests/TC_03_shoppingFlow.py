import unittest

from POMProject.Pages.address import AddressPage
from POMProject.Pages.cartModal import CartModal
from POMProject.Pages.homePage import HomePage
from POMProject.Pages.productList import ProductListPage
from POMProject.Pages.payment import PaymentPage
from POMProject.Pages.productDetails import ProductDetailsPage
from POMProject.Pages.shipping import ShippingPage
from POMProject.Pages.signInPage import SignInPage
from POMProject.Pages.cartSummary import CartSummaryPage
from POMProject.Utils.MainTest import MainTest
import time


class SearchCategoryTest(MainTest):

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
