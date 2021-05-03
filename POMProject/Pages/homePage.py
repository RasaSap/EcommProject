from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.header_sign_in_xpath = "//a[@class='login']"
        self.header_sign_out_xpath = "//a[@class='logout']"
        self.header_user_info_xpath = "//div[@class='header_user_info']//span"
        self.header_logo_xpath = "//div[@id='header_logo']"

        self.search_input_id = "search_query_top"
        self.search_button_xpath = "//form[1]/button[1]"
        self.images_in_slider_row_xpath = "//div[@id='slider_row']//img"
        self.slider_arrow_previous_xpath = "//a[@class ='bx-prev']"
        self.slider_arrow_next_xpath = "//a[@class ='bx-next']"
        self.popular_tab_xpath = "//a[@class='homefeatured']"
        self.best_sellers_tab_xpath = "//a[@class='blockbestsellers']"
        self.product_container_xpath = "//div[@id='center_column']//div[@class='product-container']//a[@class='product_img_link']"

    def check_if_element_exists(self, element_xpath):
        try:
            self.driver.find_element_by_xpath(element_xpath)
            return True
        except NoSuchElementException:
            return False

    def get_user_name_in_header(self):
        return self.driver.find_element_by_xpath(self.header_user_info_xpath).text

    def click_sign_in(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.header_sign_in_xpath))).click()

    def click_sign_out(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.search_button_xpath))).click()

    def search_category(self, category):
        self.driver.find_element_by_id(self.search_input_id).clear()
        self.driver.find_element_by_id(self.search_input_id).send_keys(category)
        self.driver.find_element_by_xpath(self.search_button_xpath).click()

    def is_slider_arrow_previous_enabled(self):
        return EC.element_to_be_clickable((By.XPATH, self.slider_arrow_previous_xpath))

    def is_slider_arrow_next_enabled(self):
        return EC.element_to_be_clickable((By.XPATH, self.slider_arrow_next_xpath))

    def is_popular_tab_exists(self):
        return self.check_if_element_exists(self.popular_tab_xpath)

    def click_popular_tab(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.popular_tab_xpath))).click()

    def popular_products(self):
        self.click_popular_tab()
        products = self.driver.find_elements_by_xpath(self.product_container_xpath)
        return products

    def is_best_sellers_tab_exists(self):
        return self.check_if_element_exists(self.best_sellers_tab_xpath)

    def click_best_sellers_tab(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.best_sellers_tab_xpath))).click()

    def best_sellers_products(self):
        self.click_best_sellers_tab()
        products = self.driver.find_elements_by_xpath(self.product_container_xpath)
        return products

    def is_header_logo_present(self):
        return self.check_if_element_exists(self.header_logo_xpath)

    def are_links_in_slider_row_valid(self):
        self.valid = False
        links = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_any_elements_located((By.XPATH, self.images_in_slider_row_xpath)))
        print("Number of links : %s" % len(links))
        for link in links:
            r = requests.head(link.get_attribute('src'))
            print(link.get_attribute('src'), r.status_code)
            if (requests.head(link.get_attribute('src')).status_code == 200):
                valid = True
            else:
                valid = False

        if valid:
            return True
        else:
            return False
