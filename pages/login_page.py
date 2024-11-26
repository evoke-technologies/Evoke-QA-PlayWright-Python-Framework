from playwright.sync_api import Page
from selenium.webdriver.common.by import By

from utils.element_utils import click , enter_text

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = 'input[id="email"]'
        self.password_input = 'input[id="password"]'
        self.login_button = 'button[id="login"]'

    def login(self, username: str, password: str):
        """Performs the login action."""
        enter_text(self.page,self.email_input,username,username)
        # send_keys(self.page, self.email_input, username)
        enter_text(self.page, self.password_input, password,password)
        click(self.page, self.login_button,self.login_button)

    # def get_error_message(self):
    #     """Returns the error message after an unsuccessful login."""
    #     return self.page.locator(self.error_message).text_content()
