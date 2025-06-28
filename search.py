import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
path = "C:\\Python313\\chromedriver-win64\\chromedriver.exe"
term = input("Enter your search term: ")
driver = webdriver.Chrome(service=Service(path))
driver.get("https://www.flipkart.com")
try:
    driver.find_element(By.XPATH, "//button[contains(text(), 'Accept')]").click()
except:
    pass
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys(term)
search_box.send_keys(Keys.RETURN)
time.sleep(5)  
driver.quit()
