from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()
		
	def test_can_start_a_list_and_retrieve_it_later(self):
		# User visits the web page
		self.browser.get('http://localhost:8000')

		# User notices the page title
		self.assertInt('To-Do', self.browser.title)
		self.fail('Finish the test!')

		# User is invited to enter a to-do item


		# User types "buy peacock feathers" into a text box


		# When the user hits enter, the page updates and lists the item


		# There is still a text box allowing the user to enter another item
		# The user enters a second item


		# The page updates and shows both items


		# The site then generates an unique URL for the list, with some explanation text


		# User visits the URL, the to-do list is there


if __name__ == '__main__':
	unittest.main(warnings='ignore')
		

