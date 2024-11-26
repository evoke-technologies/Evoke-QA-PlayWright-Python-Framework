from openpyxl.worksheet import page
from playwright.sync_api import Page
from utils.element_utils import click , enter_text

class FundtransferPage:
    def __init__(self, page: Page):
        self.page = page
        self.accountNumber_tile = 'p[id="accountNo"]'
        self.fundtrasfer_tab = 'a:text("Fund Transfers")'
        self.accountNumber_input = '(//input[@placeholder="Enter Account Number"])[1]'
        self.reEnterAccountNumber_input = '(//input[@placeholder="Enter Account Number"])[2]'

    def Fundtransfer(self, account_number: str, reEnter_number: str):
        """Performs the fund trasfer action."""
        click(self.page, self.accountNumber_tile, self.accountNumber_tile)
        click(self.page, self.fundtrasfer_tab, self.fundtrasfer_tab)
        enter_text(self.page,self.accountNumber_input,account_number,account_number)
        enter_text(self.page, self.reEnterAccountNumber_input, reEnter_number,reEnter_number)


