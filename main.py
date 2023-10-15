from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from requests import Session
from bs4 import BeautifulSoup
from json import loads
import pandas as pd
from os import system
from env import USERNAME, PASSWORD, NAMA_FILE, LENGTH, URL_ENRICHMENT_APPS, URL_STUDENT_JOBS_TABLE
import openpyxl
from config.init_buttons import LoginPageElements
from config.get_cookies import LoginProcess

def banner():
	text = '''
   /$$$$$$                                          /$$$$$$           
  /$$__  $$                                        /$$__  $$          
 | $$  \\__/  /$$$$$$$  /$$$$$$  /$$$$$$   /$$$$$$ |__/  \\ $$  /$$$$$$ 
 |  $$$$$$  /$$_____/ /$$__  $$|____  $$ /$$__  $$   /$$$$$/ /$$__  $$
  \\____  $$| $$      | $$  \\__/ /$$$$$$$| $$  \\ $$  |___  $$| $$  \\__/
  /$$  \\ $$| $$      | $$      /$$__  $$| $$  | $$ /$$  \\ $$| $$      
 |  $$$$$$/|  $$$$$$$| $$     |  $$$$$$$| $$$$$$$/|  $$$$$$/| $$      
  \\______/  \\_______/|__/      \\_______/| $$____/  \\______/ |__/      
                                        | $$                          
         [ 0xd1m5@gmail.com ]           | $$                   
               [ v0.1 ]                 |__/
'''
	print(text)

def main():
	system("cls||clear")

	banner()

	firefox_options = Options()
	firefox_options.add_argument('--headless')

	driver = webdriver.Firefox(options=firefox_options)

	login_page = LoginPageElements(driver)

	login_process = LoginProcess(driver, login_page)
	login_process.login(URL_ENRICHMENT_APPS, f"{USERNAME}@binus.ac.id", PASSWORD)

	session_cookie = login_process.get_session_cookie()
	print(" [+] berhasil mendapatkan cookie")

	driver.quit()

	session = Session()

	print(" [+] proses set cookie")
	for cookie in session_cookie:
		session.cookies.set(cookie['name'], cookie['value'])

	print(" [+] berhasil set cookie")

	data = {
	    'draw': '2',
	    'start': '0',
	    'length': f'{LENGTH}',
	    'columns[0][data]': '',
	    'columns[0][name]': '',
	    'columns[0][searchable]': 'true',
	    'columns[0][orderable]': 'true',
	    'columns[0][search][value]': '',
	    'columns[0][search][regex]': 'false',
	    'columns[1][data]': '',
	    'columns[1][name]': '',
	    'columns[1][searchable]': 'true',
	    'columns[1][orderable]': 'true',
	    'columns[1][search][value]': '',
	    'columns[1][search][regex]': 'false',
	    'columns[2][data]': '',
	    'columns[2][name]': '',
	    'columns[2][searchable]': 'true',
	    'columns[2][orderable]': 'true',
	    'columns[2][search][value]': '',
	    'columns[2][search][regex]': 'false',
	    'search[value]': '',
	    'search[regex]': 'false',
	    'order[0][column]': '0',
	    'order[0][dir]': 'asc'
	}

	print(" [+] proses request data job")
	response = session.post(URL_STUDENT_JOBS_TABLE, data=data)

	if response.status_code == 200:
		print(" [+] scraping berhasil")
		print(" [+] berhasil mendapatkan data job")

	res = loads(response.text)

	jumlah_perusahaan = res["recordsTotal"]
	list_perusahaan = res["data"]
	list_jumlah_perusahaan = len(res["data"])

	df = pd.DataFrame(list_perusahaan)

	df = df[[
	    'companyName', 'workStatus', 'position',
	    'available', 'quota', 'province', 'city',
	    'district', 'subdistrict', 'address', 'isMinimalGPA'
	]]

	print(" [+] proses menyimpan data job ke file .xlsx")

	# Membuat file Excel dengan openpyxl
	df.to_excel(f'{NAMA_FILE}.xlsx', index=False, engine='openpyxl')
	
	print(" [+] berhasil menyimpan data job ke file .xlsx")

	session.get("https://internship.apps.binus.ac.id/Login/Auth/Logout")
	print(" [+] berhasil keluar dari akun anda!")

	print(f" [#] file berhasil disimpan dengan nama: {NAMA_FILE}.xlsx")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit(1)
