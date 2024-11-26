import re

import pandas as pd
import pytest
from playwright.sync_api import sync_playwright

from pages.fundtransfer_page import FundtransferPage
from pages.login_page import LoginPage
from utils.config_utils import read_config


data = pd.read_excel('TestData.xlsx')

# Convert the rows into a list of tuples for parametrize
test_data = [(str(row['AccountNumber']), str(row['Re-EnterAccoutnNumber'])) for _, row in data.iterrows()]


@pytest.fixture(scope="function")
def setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # set headless=True to run without a browser window
        page = browser.new_page()
        page.goto(read_config('base','BASE_URL'))
        yield page
        browser.close()

@pytest.mark.parametrize("account_number, reEnter_number", test_data)
def test_successful_login(setup,account_number, reEnter_number):
    page = setup
    login_page = LoginPage(page)
    fundtransfer_page = FundtransferPage(page)

    login_page.login(read_config('base','USERNAME'),read_config('base','PASSWORD'))
    fundtransfer_page.Fundtransfer(account_number, reEnter_number)
    page.wait_for_timeout(5000)



  #  assert home_page.get_welcome_message() == f'Welcome, {USERNAME}!'

