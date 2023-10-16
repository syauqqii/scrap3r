from os import getenv
from dotenv import load_dotenv
from random import randint

# env_loaders.py
class EnvLoaders:
    # init file env, default path = ../.env
    def __init__(self, env_path="../.env"):
        self.env_path = env_path
        self.loaded = False

    # function: process load file .env
    def load_env(self):
        if not self.loaded:
            load_dotenv(self.env_path)
            self.loaded = True

    # function: return text (x from .env)
    def get_variable(self, variable_name):
        self.load_env()
        return getenv(variable_name)

    # function: return call function (username email from .env)
    def get_username(self):
        return self.get_variable("EMAIL_BINUS")

    # function: return call function (password from .env)
    def get_password(self):
        return self.get_variable("PASSWORD")

    # function: return call function get_password (encrypted text: *)
    def get_encrypted_password(self):
        text = ""
        for _ in range(len(self.get_password())):
            text += "*"

        text += "*" * randint(1, 7)
        return text

    def get_file_name(self):
        return self.get_variable("NAMA_FILE")

    # function: return call function (number GUI MODE from .env)
    def get_gui_mode(self):
        return self.get_variable("GUI_MODE")

    def get_url_enrichment(self):
        return self.get_variable("LOGIN_URL_ENRICHMENT_APP")

    def get_url_table_jobs(self):
        return self.get_variable("URL_STUDENT_JOBS_TABLE")