import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
s=Service(r"C:\pythondrivers\msedgedriver.exe")
driver=webdriver.Edge(service=s)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, ".oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button"))
# ).click()
time.sleep(5)
driver.find_element(By.NAME,"username").send_keys("Admin")
# driver.find_element(By.CLASS_NAME,"oxd-button oxd-button--medium oxd-button--main orangehrm-login-button").click()