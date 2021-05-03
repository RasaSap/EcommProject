class SignInPage:

    def __init__(self, driver):
        self.driver = driver

        self.email_textbox_xpath = "//input[@id='email']"
        self.password_textbox_xpath = "//input[@id='passwd']"
        self.sign_in_button_xpath = "//button[@id='SubmitLogin']"

    def enter_email(self, email):
        self.driver.find_element_by_xpath(self.email_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.email_textbox_xpath).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)

    def click_sign_in(self):
        self.driver.find_element_by_xpath(self.sign_in_button_xpath).click()
