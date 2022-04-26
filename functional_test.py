import time

from selenium import webdriver
import unittest

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=r'D:\Google Driver\chromedriver.exe')

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title), "Browser title was:" + self.browser.title
        self.fail('Finish the test!')

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')
        # She notices the page title and header mention to - do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)
        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEquall(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
        # She types "Buy peacock feathers" into a text box(Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')
        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to - do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        table = self.browser.find_element(By.ID, 'id list table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
            )
        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very methodical)
        self.fail( 'Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
# Edith has heard about a cool new online to-do app. She goes
# to check out its homepage
# She notices the page title and header mention to-do lists

# She is invited to enter a to-do item straight away
# She types "Buy peacock feathers" into a text box (Edith's hobby
# is tying fly-fishing lures)
# When she hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a to-do list
# There is still a text box inviting her to add another item. She
# enters "Use peacock feathers to make a fly" (Edith is very methodical)
# The page updates again, and now shows both items on her list
# Edith wonders whether the site will remember her list. Then she sees
# that the site has generated a unique URL for her -- there is some
# explanatory text to that effect.
# She visits that URL - her to-do list is still there.
# Satisfied, she goes back to sleep

# self.browser = webdriver.Chrome(executable_path=r'D:\Google Driver\chromedriver.exe') # 浏览器驱动
