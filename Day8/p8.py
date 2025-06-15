import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service(r"C:\pythondrivers\chromedriver-win64\chromedriver.exe")
d=webdriver.Chrome(service=s)
# d.get("https://www.facebook.com/")
d.get("https://demo.nopcommerce.com/register?returnUrl=%2Flogin")
d.maximize_window()
time.sleep(3)
e=d.find_element(By.XPATH,"//a[normalize-space()='Register']")
e.click()
time.sleep(3)
d.get("https://www.facebook.com/")
# Application commands
# print(d.title)
# print(d.current_url)
# print(d.page_source)

# j=d.find_element(By.XPATH,"//input[@id='small-searchterms']")
# print(j.is_displayed())
#
# print(j.is_enabled())
# m=d.find_element(By.XPATH,"//input[@id='gender-male']")
# f=d.find_element(By.XPATH,"//input[@id='gender-female']")
# print(m.is_selected())
# m.click()
# print(m.is_selected())
time.sleep(3)
d.back()
time.sleep(3)
d.forward()
time.sleep(3)
d.refresh()
