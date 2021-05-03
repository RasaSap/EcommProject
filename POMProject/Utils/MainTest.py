import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from selenium import webdriver

class MainTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path=r'C:\Users\oska\PycharmProjects\EcommProject\drivers\chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("http://automationpractice.com/index.php")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
