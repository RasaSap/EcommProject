from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ProductDetailsPage:

    def __init__(self, driver):
        self.driver = driver

        self.product_image_xpath = "//img[@id='bigpic']"
        self.product_price_xpath = "//span[@id='our_price_display']"
        self.quantity_minus_xpath = "//i[@class='icon-minus']"
        self.quantity_up_xpath = "//a[@class='btn btn-default button-plus product_quantity_up']"
        self.select_size_xpath = "//select[@class='form-control attribute_select no-print']"
        self.button_add_to_cart_xpath = "//span[contains(text(),'Add to cart')]"
        self.view_larger_img_xpath = "//span[@class='span_link no-print']"
        self.close_img_xpath = "//a[@class='fancybox-item fancybox-close']"
        self.select_size_xpath = "//div[@id='uniform-group_1']"

    def click_add_to_cart_button(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.button_add_to_cart_xpath))).click()

    def click_view_larger_img(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.view_larger_img_xpath))).click()

    def click_close_img(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.close_img_xpath))).click()

    def get_product_price(self):
        price_with_dollar = self.driver.find_element_by_xpath(self.product_price_xpath).text
        return price_with_dollar[1:len(price_with_dollar)]

    def click_quantity_up(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.quantity_up_xpath))).click()

    def choose_size(self, size):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.select_size_xpath))).click()
        time.sleep(1)
        option = self.driver.find_element_by_xpath("//select/option[text()='" + size + "']")
        option.click()
        self.driver.find_element_by_xpath(self.select_size_xpath).click()
