from utils.banner import Banner
from utils.envLoaders import EnvLoaders
from utils.helpers import Helpers
from controllers.authentication import Authentication
from models.buttons import Buttons
from models.data import Data

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from requests import Session
from json import loads
import pandas as pd
import openpyxl

# Load ENV
env = EnvLoaders(".env")

# Memanggil function get_x (return type: text) pada class EnvLoader yang ada di utils
USERNAME = env.get_username()
PASSWORD = env.get_password()
GUI_MODE = env.get_gui_mode()

NAMA_FILE = env.get_file_name()

LOGIN_URL_ENRICHMENT_APP = env.get_url_enrichment()
URL_STUDENT_JOBS_TABLE = env.get_url_table_jobs()

DATA = Data().get_data()

def main():
	# Memanggil function clear_screen pada class Helpers yang ada di utils
	Helpers().clear_screen()

	if int(GUI_MODE) == 0:
		print(Banner("OFF").print_banner())
		firefox_options = Options()
		firefox_options.add_argument('--headless')

		driver = webdriver.Firefox(options=firefox_options)
	elif int(GUI_MODE) == 1:
		print(Banner("ON").print_banner())
		driver = webdriver.Firefox()
	else:
		print(" [!] Set GUI_MODE di .env anda antara 0/1.")
		exit(1)

	login_page = Buttons(driver)

	login_process = Authentication(driver, login_page)
	login_process.login(LOGIN_URL_ENRICHMENT_APP, USERNAME, PASSWORD)

	session_cookie = login_process.get_cookie()
	print(" [+] berhasil mendapatkan cookie")

	driver.quit()

	session = Session()

	print(" [+] proses set cookie")
	for cookie in session_cookie:
		session.cookies.set(cookie['name'], cookie['value'])

	print(" [+] berhasil set cookie")

	print(" [+] proses request data job")
	response = session.post(URL_STUDENT_JOBS_TABLE, data=DATA)

	if response.status_code == 200:
		print(" [+] scraping berhasil")
		print(" [+] berhasil mendapatkan data job")

	res = loads(response.text)

	jumlah_perusahaan = res["recordsTotal"]
	list_perusahaan = res["data"]
	list_jumlah_perusahaan = len(res["data"])

	df = pd.DataFrame(list_perusahaan)

	df = df[[
	    'companyName', 'workStatus', 'position', 'available', 'quota',
	    'desc', 'jobReq', 'province', 'city',
	    'district', 'subdistrict', 'address', 'isMinimalGPA'
	]]

	print(" [+] proses menyimpan data job ke file .xlsx")

	# Membuat file Excel dengan openpyxl
	df.to_excel(f'{NAMA_FILE}.xlsx', index=False, engine='openpyxl')
	
	print(" [+] berhasil menyimpan data job ke file .xlsx")

	session.get("https://internship.apps.binus.ac.id/Login/Auth/Logout")
	print(" [+] berhasil keluar dari akun anda!")

	print(f"\n [#] file berhasil disimpan dengan nama: {NAMA_FILE}.xlsx")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit(1)
