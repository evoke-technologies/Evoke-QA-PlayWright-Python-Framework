import shutil
from datetime import datetime

import allure
import os

import allure
from playwright.sync_api import Page
from selenium.webdriver.remote.webdriver import WebDriver


def cleanup_files(directory: str):
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)

# def attach_screenshot(driver: WebDriver, name: str):
#
#     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#     screenshot = driver.get_screenshot_as_png()
#     allure.attach(
#         screenshot,
#         name=f"{name}_{timestamp}",
#         attachment_type=allure.attachment_type.PNG
#     )

def attach_screenshot(page: Page, name: str):
    """Attach a screenshot of the current page to Allure."""
    try:
        # Generate a timestamp for the screenshot name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Capture screenshot as a PNG
        screenshot = page.screenshot(full_page=True)  # Capture the full page screenshot

        # Attach the screenshot to Allure
        allure.attach(
            screenshot,
            name=f"{name}_{timestamp}",
            attachment_type=allure.attachment_type.PNG
        )
    except Exception as e:
        print(f"Failed to take screenshot: {e}")

def log_status(status: str, message: str, driver: WebDriver = None):
        """
        Log the test status and attach a screenshot if provided.
        :param status: The status of the test (e.g., "PASS", "FAIL")
        :param message: The message to log
        :param driver: The Selenium WebDriver instance (optional)
        """
        if driver:
            attach_screenshot(driver, f"{status} - {message}")
        # if status == "PASS":
        #     allure.attach(
        #         body=message,
        #         name="Test Status",
        #         attachment_type=allure.attachment_type.TEXT
        #     )
        # elif status == "FAIL":
        #     allure.attach(
        #         body=message,
        #         name="Test Status",
        #         attachment_type=allure.attachment_type.TEXT
        #     )
