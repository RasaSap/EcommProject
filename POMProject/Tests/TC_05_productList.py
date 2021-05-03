import unittest
from POMProject.Pages.homePage import HomePage
from POMProject.Pages.productList import ProductListPage
from POMProject.Utils.MainTest import MainTest
import softest


class ProductListTest(MainTest):

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
