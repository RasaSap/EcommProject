from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddressPage:

    def __init__(self, driver):
        self.driver = driver

        self.button_proceed_checkout_xpath = "//button[@name='processAddress']"

    def click_proceed_to_checkout(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.button_proceed_checkout_xpath))).click()
