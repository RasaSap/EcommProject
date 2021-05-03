from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShippingPage:

    def __init__(self, driver):
        self.driver = driver

        self.terms_checkbox_xpath = "//input[@id='cgv']"
        self.button_proceed_checkout_xpath = "//button[@name='processCarrier']"

    def click_terms_of_service_checkbox(self):
        self.driver.find_element_by_xpath(self.terms_checkbox_xpath).click()

    def click_proceed_to_checkout(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.button_proceed_checkout_xpath))).click()
