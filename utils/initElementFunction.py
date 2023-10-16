from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# initElementFunction.py
class ElementFunction:
	# init webdriver & request timeout
	def __init__(self, driver, timeout=60):
		self.driver = driver
		self.timeout = timeout

	# function: find element with 2 args (method, button_element)
	def find_element(self, by, value):
		return WebDriverWait(self.driver, self.timeout).until(
			EC.presence_of_element_located((by, value))
		)

	# function: wait until element begin, with 3 args (method, button_element, text element)
	def wait_find_element(self, by, value, text):
		return WebDriverWait(self.driver, self.timeout).until(
			EC.text_to_be_present_in_element((by, value), text)
		)