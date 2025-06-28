from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Step 1: Launch the browser
driver = webdriver.Chrome()
driver.maximize_window()


# Step 2: Navigate to the dropdown page
driver.get("https://the-internet.herokuapp.com/dropdown")
time.sleep(2)


# Step 3: Locate the dropdown element
dropdown_element = driver.find_element(By.ID, "dropdown")

# Step 4: Create a Select object
select = Select(dropdown_element)

# --- Select Methods ---

# 1. Select by visible text
select.select_by_visible_text("Option 1")
time.sleep(1)

# 2. Select by index (Index starts at 0, so Option 1 is index 1)
select.select_by_index(1)
time.sleep(1)

# 3. Select by value (check HTML, Option 1 has value="1", Option 2 has value="2")
select.select_by_value("1")
time.sleep(1)


# --- Count dropdown values ---
options = select.options
option_count = len(options)
expected_count = 3   # Includes the default "Please select an option"

if option_count == expected_count:
    print("Test case passed. Count is correct.")
else:
    print(f"Test case failed. Expected {expected_count}, but got {option_count}")



# --- Loop through dropdown options and select a target if found ---
target_value = "Option 2"
found = False

for option in options:
    if option.text.strip() == target_value:
        option.click()
        print(f"Selected option: {target_value}")
        found = True
        break

if not found:
    print(f"Option '{target_value}' not found in dropdown.")


# Final wait and quit
time.sleep(2)
driver.quit()
