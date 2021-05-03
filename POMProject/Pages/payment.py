from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PaymentPage:

    def __init__(self, driver):
        self.driver = driver

        self.bank_payment_xpath = "//a[@class='bankwire']"
        self.button_confirm_order_xpath = "//button[@class='button btn btn-default button-medium']"
        self.order_confirmation_message_xpath = "//p[@class='cheque-indent']"

    def click_pay_by_bank(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.bank_payment_xpath))).click()

    def click_confirm_order(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.button_confirm_order_xpath))).click()

    def get_order_confirmation_message(self):
        return self.driver.find_element_by_xpath(self.order_confirmation_message_xpath).text






