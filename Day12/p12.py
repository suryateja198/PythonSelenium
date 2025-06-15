import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s=Service(r"C:\pythondrivers\chromedriver-win64\chromedriver.exe")
d=webdriver.Chrome(service=s)
d.get("https://www.facebook.com/")

d.find_element(By.CSS_SELECTOR,"#email").send_keys("SURYATEJA123.com")
time.sleep(3)
# i=d.find_elements(By.TAG_NAME,"input")
# print(len(i))
# d.find_element(By.LINK_TEXT,"Forgotten password?").click()
d.find_element(By.PARTIAL_LINK_TEXT,"Forgotten").click()
time.sleep(2)

d.find_elements(By.CLASS_NAME,"")

