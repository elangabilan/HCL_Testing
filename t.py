from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Replace this with your actual path
path = "C:\Python313\chromedriver-win64\chromedriver.exe"

driver = webdriver.Chrome(service=Service(path))
driver.get("https://www.google.com")
print("Page Title:", driver.title)
driver.quit()
