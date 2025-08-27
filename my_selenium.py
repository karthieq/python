from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.maximize_window()

driver.get("https://www.saucedemo.com/v1/")
time.sleep(3)

# driver.find_element(By.ID, "user-name").send_keys("standard_user")
# driver.find_element(By.ID, "password").send_keys("secret_sauce")
# driver.find_element(By.ID, "login-button").click()

input_element = driver.find_element(By.XPATH, "//input[@id='user-name']")
# print(dir(input_element))
input_element.send_keys("standard_user")
time.sleep(3)

input_element = driver.find_element(By.XPATH, "//input[@id='password']")
input_element.send_keys("secret_sauce")
time.sleep(3)

input_element = driver.find_element(By.XPATH, "//input[@id='login-button']")
input_element.click()
time.sleep(3)

# input_element = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[3]/button")
# input_element.click()
# time.sleep(3)


driver.quit()
