import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
help(selenium.webdriver.chrome.service)
from selenium.webdriver.common.by import By

# s=Service("C:\pythondrivers\chromedriver-win64\chromedriver.exe")
#
# d=webdriver.Chrome(service=s)
#
# d.get("https://www.facebook.com/")
#
# time.sleep(3)
#
# d.find_element(By.NAME,"email").send_keys("hellomail")
# time.sleep(3)
# d.find_element(By.ID,"pass").send_keys("surya")
# time.sleep(5)
# d.find_element(By.NAME,"login").click()
# time.sleep(50)