from utils.initElementFunction import ElementFunction

from selenium.webdriver.common.by import By

# buttons.py
class Buttons:
    def __init__(self, driver):
        self.driver = driver
        self.element_function = ElementFunction(driver)

    def find_title_element_username(self):
        return self.element_function.wait_find_element(By.CSS_SELECTOR, 'div[data-bind="text: title"]', "Sign in")

    def find_title_element_password(self):
        return self.element_function.wait_find_element(By.CSS_SELECTOR, 'div[data-bind="text: str[\'CT_PWD_STR_EnterPassword_Title\']"]', "Enter password")

    def find_title_element_save(self):
        return self.element_function.wait_find_element(By.CSS_SELECTOR, 'div[data-bind="text: str[\'STR_Kmsi_Title\']"]', "Stay signed in?")

    def find_button_orange_dashboard(self):
        return self.element_function.wait_find_element(By.CSS_SELECTOR, 'span[class="position"] strong', "ENRICHMENT TRACK")

    def find_text_dashboard(self):
        return self.element_function.wait_find_element(By.CSS_SELECTOR, 'h2[class="no-padding"]', "ACTIVE JOB APPLICATION")

    # element untuk mencari button: login (direct ke form login)
    def find_button_login(self):
        return self.element_function.find_element(By.CSS_SELECTOR, 'button[id="btnLogin"]')

    # element untuk mencari input: username
    def find_username_input(self):
        return self.element_function.find_element(By.CSS_SELECTOR, 'input[id="i0116"]')

    # element untuk mencari input: password
    def find_password_input(self):
        return self.element_function.find_element(By.CSS_SELECTOR, 'input[id="i0118"]')

    # element untuk mencari button: selanjutnya (submit)
    def find_submit_button(self):
        return self.element_function.find_element(By.CSS_SELECTOR, 'input[id="idSIButton9"]')

    # element untuk mencari button: tidak (Tetap masuk? tidak.)
    def find_back_button(self):
        return self.element_function.find_element(By.CSS_SELECTOR, 'input[id="idBtn_Back"]')

    def find_orange_button(self):
        return self.element_function.find_element(By.CSS_SELECTOR, 'a[class="button button-orange"]')