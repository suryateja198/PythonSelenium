import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service(r"C:\pythondrivers\chromedriver-win64\chromedriver.exe")
d=webdriver.Chrome(service=s)
d.get("https://www.facebook.com/")
h=d.find_element(By.XPATH,"//input[@id='email']")
print(h.text)
h.send_keys("hello")
print(h.get_attribute())
