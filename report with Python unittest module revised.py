import unittest
import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class jobSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_job(self):
        driver = self.driver
        driver.get("https://www.glassdoor.com/index.htm")
        self.assertIn("Glassdoor", driver.title)
        elem = driver.find_element_by_name("sc.keyword")
        elem.send_keys("Quality")
        elem.send_keys(Keys.RETURN)
        #assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    HTMLTestRunner.main()
