from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from multiprocessing import Process
import time

# === Driver functions for each browser ===

def test_chrome():
    driver = webdriver.Chrome(service=ChromeService("C:/Drivers/chromedriver.exe"))
    run_login_test(driver, "Chrome")

def test_firefox():
    driver = webdriver.Firefox(service=FirefoxService("C:/Drivers/geckodriver.exe"))
    run_login_test(driver, "Firefox")

def test_edge():
    driver = webdriver.Edge(service=EdgeService("C:/Drivers/msedgedriver.exe"))
    run_login_test(driver, "Edge")

# === Common login test logic ===

def run_login_test(driver, browser_name):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.maximize_window()
    time.sleep(2)

    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    time.sleep(2)
    if "Logged In Successfully" in driver.page_source:
        print(f"{browser_name}: ✅ Login passed")
    else:
        print(f"{browser_name}: ❌ Login failed")

    time.sleep(2)
    driver.quit()

# === Running all tests using for loop ===

test_functions = [test_chrome, test_firefox, test_edge]
processes = []

for func in test_functions:
    p = Process(target=func)
    processes.append(p)
    p.start()

for p in processes:
    p.join()
