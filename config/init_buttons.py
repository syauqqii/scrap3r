# init_buttons.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPageElements:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, value, timeout=60):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def wait_find_element(self, by, value, text, timeout=60):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((by, value), text)
        )

    def find_title_element_username(self):
        return self.wait_find_element(By.CSS_SELECTOR, 'div[data-bind="text: title"]', "Sign in")

    def find_title_element_password(self):
        return self.wait_find_element(By.CSS_SELECTOR, 'div[data-bind="text: str[\'CT_PWD_STR_EnterPassword_Title\']"]', "Enter password")

    def find_title_element_save(self):
        return self.wait_find_element(By.CSS_SELECTOR, 'div[data-bind="text: str[\'STR_Kmsi_Title\']"]', "Stay signed in?")

    def find_button_orange_dashboard(self):
        return self.wait_find_element(By.CSS_SELECTOR, 'span[class="position"] strong', "ENRICHMENT TRACK")

    def find_text_dashboard(self):
        return self.wait_find_element(By.CSS_SELECTOR, 'h2[class="no-padding"]', "ACTIVE JOB APPLICATION")

    # element untuk mencari button: login (direct ke form login)
    def find_button_login(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'button[id="btnLogin"]')

    # element untuk mencari input: username
    def find_username_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[id="i0116"]')

    # element untuk mencari input: password
    def find_password_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[id="i0118"]')

    # element untuk mencari button: selanjutnya (submit)
    def find_submit_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[id="idSIButton9"]')

    # element untuk mencari button: tidak (Tetap masuk? tidak.)
    def find_back_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[id="idBtn_Back"]')

    def find_orange_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'a[class="button button-orange"]')
