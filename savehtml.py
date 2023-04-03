import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# Set the path to the ChromeDriver executable
chromedriver_path = "path/to/chromedriver"  # Update this to the path of your ChromeDriver

# Connect to the existing Chrome instance
driver = webdriver.Chrome(chromedriver_path, options=chrome_options)

# Save the HTML content of each open tab
for window_handle in driver.window_handles:
    driver.switch_to.window(window_handle)
    url = driver.current_url
    html_content = driver.page_source

    # Save the HTML content to a file
    file_name = f"{time.time()}.html"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(html_content)

driver.quit()
