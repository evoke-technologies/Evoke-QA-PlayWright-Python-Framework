from telnetlib import EC

from playwright.sync_api import Page, TimeoutError
from playwright.sync_api import Page
from selenium.webdriver.support.wait import WebDriverWait

from utils.allure_utils import log_status


# def send_keys(page: Page, locator: str, text: str):
#     """Fills the text input field with the provided value."""
#     element = page.locator(locator)
#     element.fill(text)

def click(page: Page, locator: str, text: str):
    """Clicks on an element identified by the locator."""
    try:
         element = page.locator(locator)
         element.click()
         page.wait_for_timeout(5000)
         log_status("PASS", f"Successfully clicked on '{text}' field", page)

    except TimeoutError as e:
        # Handle timeout if the element is not found or visible in time
        log_status("FAIL", f"Failed to click on '{text}' in '{locator}' field: Timeout error", page)
        raise e
    except Exception as e:
        # Catch any other exception and log the failure
        log_status("FAIL", f"Failed to click on '{text}' in '{locator}' field: {str(e)}", page)
        raise e

def enter_text(page: Page, locator: str, text: str, element_name: str):
    """Enters text into an input field with error handling and logging."""
    try:
        # Wait for the element to be visible before interacting with it
        element = page.locator(locator)
        element.wait_for(state="visible", timeout=20000)  # Wait up to 10 seconds

        # Clear the input field and enter the text
        element.fill('')  # Clears the text
        element.fill(text)  # Enters the text

        # Log success message
        log_status("PASS", f"Successfully entered '{text}' in '{element_name}' field", page)

    except TimeoutError as e:
        # Handle timeout if the element is not found or visible in time
        log_status("FAIL", f"Failed to enter '{element_name}' in '{locator}' field: Timeout error", page)
        raise e
    except Exception as e:
        # Catch any other exception and log the failure
        log_status("FAIL", f"Failed to enter '{element_name}' in '{locator}' field: {str(e)}", page)
        raise e
