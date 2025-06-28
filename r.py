from selenium import webdriver
from selenium.webdriver.common.by import By  # Fix the import

# Set up the Firefox driver
driver = webdriver.Firefox()
driver.maximize_window()

# Login credentials and URL
username = "standard_user"
password = "secret_sauce"
login_url = "https://www.saucedemo.com/"

# Open the login page
driver.get(login_url)

# Locate username and password fields
username_field = driver.find_element(By.ID, "user-name")  # Fixed syntax
password_field = driver.find_element(By.ID, "password")   # Fixed syntax

# Enter credentials
username_field.send_keys(username)
password_field.send_keys(password)  # Fixed: was sending password to username_field

# Locate and click the login button
login_button = driver.find_element(By.ID, "login-button")  # Fixed name and syntax

# Assert the login button is enabled
assert login_button.get_attribute("disabled") is None  # Use correct logic and variable name

# Click the button
login_button.click()
