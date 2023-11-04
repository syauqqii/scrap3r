class Authentication:
	def __init__(self, driver, login_page):
		self.driver = driver
		self.login_page = login_page

	def login(self, url, username, password):
		print("\n [+] menuju login page")
		self.driver.get(url)
		print(f" [+] proses login ke {url}")

		login_button = self.login_page.find_button_login()
		login_button.click()

		self.login_page.find_title_element_username()

		print(" [+] proses input email")
		try:
			username_input = self.login_page.find_username_input()
		except:
			username_input = self.login_page.find_username_input_id()

		# input email
		username_input.send_keys(username)

		print(" [+] proses tekan selanjutnya")
		submit_button = self.login_page.find_submit_button()
		submit_button.click()

		self.login_page.find_title_element_password()

		print(" [+] proses input password")
		try:
			password_input = self.login_page.find_password_input()
		except:
			password_input = self.login_page.find_password_input_id()

		# input password
		password_input.send_keys(password)

		print(" [+] proses tekan masuk")
		submit_button = self.login_page.find_submit_button()
		submit_button.click()

		print(" [+] proses tolak simpan data login")

		self.login_page.find_title_element_save()

		# cancel validation login
		try:
			back_button = self.login_page.find_back_button()
		except:
			back_button = self.login_page.find_back_button_id()

		back_button.click()

		print(" [+] proses masuk ke dashboard")
		self.login_page.find_button_orange_dashboard()

		print(" [+] proses login berjalan dengan sukses")

		print(" [+] proses menuju dashboard internship")
		orange_button = self.login_page.find_orange_button()
		self.driver.execute_script("arguments[0].click();", orange_button)

		print(" [+] berhasil menuju dashboard internship")
		self.login_page.find_text_dashboard()

	def get_cookie(self):
		print(" [+] proses mendapatkan cookie")
		return self.driver.get_cookies()
