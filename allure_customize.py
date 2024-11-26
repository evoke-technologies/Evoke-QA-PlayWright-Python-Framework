import shutil
import os


def replace_allure_logo(allure_report_dir, custom_logo_path):
    """
    Replace the default Allure logo with a custom logo.
    :param allure_report_dir: Path to the Allure report directory.
    :param custom_logo_path: Path to the custom logo image.
    """
    # Path to the Allure assets directory
    assets_dir = os.path.join(allure_report_dir, 'assets')

    # Check if assets folder exists, if not, create it
    if not os.path.exists(assets_dir):
        os.makedirs(assets_dir)

    # Define the path where the logo should be placed in Allure report
    custom_logo_dest = os.path.join(assets_dir, 'custom_logo.png')

    # Replace the default logo with the custom logo
    shutil.copy(custom_logo_path, custom_logo_dest)
    print(f"Custom logo placed at {custom_logo_dest}")


def update_allure_index_html(allure_report_dir):
    """
    Update the Allure index.html to use the custom logo.
    :param allure_report_dir: Path to the Allure report directory.
    """
    index_html_path = os.path.join(allure_report_dir, 'index.html')

    if os.path.exists(index_html_path):
        with open(index_html_path, 'r') as file:
            html_content = file.read()

            # Define the custom logo HTML
            custom_logo_html = '<img src="assets/custom_logo.png" alt="Custom Logo" id="custom-logo" style="display:block; margin: 0 auto; max-width: 200px;">'

            # Find the closing </body> tag
            body_end_index = html_content.find('</div>')
            if body_end_index != -1:
                # Inject the custom logo before the closing </body> tag
                html_content = html_content[:body_end_index] + custom_logo_html + html_content[body_end_index:]

        # Write the updated HTML content back to the file
        with open(index_html_path, 'w') as file:
            file.write(html_content)
        print(f"Updated index.html to use the custom logo.")


def main():
    allure_results_dir = 'allure-results'  # Directory where allure-results are stored
    allure_report_dir = 'allure-report'  # Directory where allure-report is generated
    custom_logo_path = 'utils/custom_logo.png'  # Path to your custom logo

    # Step 1: Move Allure results to Allure report
    os.system(f"allure generate {allure_results_dir} --clean -o {allure_report_dir}")

    # Step 2: Replace logo in Allure report automatically
    replace_allure_logo(allure_report_dir, custom_logo_path)
    update_allure_index_html(allure_report_dir)

    # Step 3: Serve the generated report
  # os.system(f"allure serve {allure_report_dir}")

    command = '''
    pytest --alluredir=allure-results && python update_allure_logo.py
    '''

    # Execute the combined command using os.system()
    os.system(command)
   # # os.system(f"allure serve {allure_report_dir}")
   #  os.system("python update_allure_logo.py && powershell -Command '$todayDate = Get-Date -Format \"MM-dd-yyyy_HH-mm-ss-fff\"; allure generate allure-results -o \"allure-results/allure-report-$todayDate\" -clean'")


if __name__ == "__main__":
    main()
