from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartModal:

    def __init__(self, driver):
        self.driver = driver

        self.cart_modal_xpath = "//div[@id='layer_cart']"
        self.button_continue_shopping_xpath = "//div[@id='layer_cart']//span[@title='Continue shopping']"
        self.button_chek_out_xpath = "//div[@id='layer_cart']//a[@title='Proceed to checkout']"

    def click_continue_shopping(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.button_continue_shopping_xpath))).click()

    def click_proceed_to_checkout(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.button_chek_out_xpath))).click()
