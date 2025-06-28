from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get('https://www.google.com')
time.sleep(5)
b=driver.find_element(By.XPATH,'//*[@id="stUuGf"]/div/div[2]/div/div/div/div[2]/div/promo-button-text[1]/div/div').click()
A=driver.find_element(By.XPATH,'//*[@id="APjFqb"]').click()
A.send_keys("python")
a.send_keys(Keys.RETURN)


time.sleep(2)
driver.refresh()
driver.quit()
