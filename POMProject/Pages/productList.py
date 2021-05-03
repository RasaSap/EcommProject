from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductListPage:

    def __init__(self, driver):
        self.driver = driver

        self.product_image_xpath = "//a[@class='product_img_link']"
        self.products_by_grid_xpath = "//i[@class='icon-th-large']"
        self.products_by_list_xpath = "//i[@class='icon-th-list']"
        self.select_product_sort_id = "uniform-selectProductSort"
        self.sort_dropdown_item_xpath = "//select[@id='selectProductSort']/option"
        self.button_more_xpath = "//a[@class='button lnk_view btn btn-default']"

    def product_list(self):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.product_image_xpath)))
        return self.driver.find_elements_by_xpath(self.product_image_xpath)

    def check_images_number(self):
        return len(self.product_list())

    def click_first_product(self):
        images = self.driver.find_elements_by_xpath(self.product_image_xpath)
        ActionChains(self.driver).move_to_element(images[0]).pause(1).perform()
        image_hover = self.driver.find_elements_by_xpath(self.button_more_xpath)
        image_hover[0].click()

    def get_product_no_in_grid(self):
        self.driver.find_element_by_xpath(self.products_by_grid_xpath).click
        return self.check_images_number()

    def get_product_no_in_list(self):
        self.driver.find_element_by_xpath(self.products_by_list_xpath).click
        return self.check_images_number()

    def get_sort_options_number(self):
        self.driver.find_element_by_id(self.select_product_sort_id).click
        sorts = self.driver.find_elements_by_xpath(self.sort_dropdown_item_xpath)
        return len(sorts)
