from selenium import webdriver
from selenium.webdriver.common.by import By
import time  # You forgot to import this

# Launch browser
driver = webdriver.Firefox()

# Step 1: Open URL
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()

# Step 2: Wait for page to load
time.sleep(5)

# Step 3: Click "Forgot your password?" link
driver.find_element(By.CSS_SELECTOR, ".oxd-text.oxd-text--p.orangehrm-login-forgot-header").click()

# Step 4: Wait
time.sleep(5)

# Step 5: Navigate Back
driver.back()
time.sleep(5)

# Step 6: Navigate Forward
driver.forward()
time.sleep(5)

# Step 7: Refresh Page
driver.refresh()
time.sleep(5)

driver.close()
