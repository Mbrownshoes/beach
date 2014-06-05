from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    # def check_for_header_in_table(self, header_text):
    #     table = self.browser.find_element_by_id('id')


    def test_can_start_a_list_and_retrieve_it_later(self):
        #Arlo's checking out a new app that shows current water conditions at Balmy beach.
        self.browser.get('http://localhost:8000')

        # He notices the header and title mention the beach.
        self.assertIn('Balmy beach',  self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Balmy Beach', header_text)

        # He also sees in large font the air and water temperature and water quality index
        table = self.browser.find_element_by_id('id_conditions_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('Water temperature', [row.text for row in rows])
        # At the bottom there is also a 'see past conditions' button, which he presses.

        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')