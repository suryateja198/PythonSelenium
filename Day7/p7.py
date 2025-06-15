import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s=Service(r"C:\pythondrivers\chromedriver-win64\chromedriver.exe")
d=webdriver.Chrome(service=s)
d.get("https://www.facebook.com/")
d.find_element(By.NAME,"email").send_keys("hello")
time.sleep(10)