from selenium import webdriver
from selenium.webdriver.common.by import By
import requests  
import time

# 1. Initialize browser
browser = webdriver.Chrome()

# 2. Open the webpage
browser.get("https://the-internet.herokuapp.com/broken_images")
browser.maximize_window()
time.sleep(2)  # Optional wait for images to load

# 3. Get all <img> elements
images = browser.find_elements(By.TAG_NAME, "img")
broken_images = []

# 4. Loop through each image and check status
for image in images:
    src = image.get_attribute("src")
    if src:
        try:
            response = requests.get(src)
            if response.status_code != 200:
                print(f"Broken image found: {src}")
                broken_images.append(src)
        except requests.exceptions.RequestException as e:
            print(f"Error checking image {src}: {e}")
            broken_images.append(src)

# 5. Final result
if broken_images:
    print("\nList of broken images:")
    for broken_image in broken_images:
        print(broken_image)
else:
    print("No broken images found.")

# 6. Close browser
browser.quit()
