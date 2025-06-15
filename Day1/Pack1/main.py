import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s=Service(r"C:\\pythondrivers\\chromedriver-win64\\chromedriver.exe")

d=webdriver.Chrome(service=s)
d.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
d.maximize_window()
d.find_element(By.NAME,"username").send_keys("hello")
time.sleep(2)

