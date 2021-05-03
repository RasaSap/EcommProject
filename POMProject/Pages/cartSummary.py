from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartSummaryPage:

    def __init__(self, driver):
        self.driver = driver

        self.button_proceed_checkout_xpath = "//p[@class='cart_navigation clearfix']/a[@title='Proceed to checkout']"
        self.total_product_price_xpath = "//span[contains(@id,'total_product_price')]"
        self.product_color_size_xpath = "//tr[@id='product_5_23_0_0']//small/a"
        self.delete_first_product_xpath = "//tr[@id='product_2_7_0_0']/td[7]/div[1]/a[1]/i[1]"
        self.continue_shopping_xpath = "//div[1]/p[2]/a[2]"
        self.quantity_xpath = "//tr[contains(@id,'product_')]/td[5]/input[2]"

    def click_proceed_to_checkout(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.button_proceed_checkout_xpath))).click()

    def total_product_price(self):
        price_with_dollar = self.driver.find_element_by_xpath(self.total_product_price_xpath).text
        return price_with_dollar[1:len(price_with_dollar)]

    def product_size(self):
        color_size_text = self.driver.find_element_by_xpath(self.product_color_size_xpath).text
        return color_size_text[-1]

    def delete_first_product(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.delete_first_product_xpath))).click()

    def click_continue_shopping(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.continue_shopping_xpath))).click()

    def get_quantity(self):
        element = self.driver.find_element_by_xpath(self.quantity_xpath)
        return element.get_attribute("value")
