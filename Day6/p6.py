from webbrowser import Chrome

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s=Service(r"C:\pythondrivers\chromedriver-win64\chromedriver.exe")

d=webdriver.Chrome(service=s)

d.get("https://www.facebook.com/")
time.sleep(3)

d.find_element(By.NAME,"email").send_keys("hell")
d.find_element(By.ID,"email").clear()
time.sleep(3)


d.find_element(By.CSS_SELECTOR,"input#email").send_keys("mail")
time.sleep(3)
d.find_element(By.CSS_SELECTOR,"input.inputtext").clear()
#d.find_element(By.CSS_SELECTOR,"input[id=email]").send_keys("this is tag and attribute")
d.find_element(By.CSS_SELECTOR,"input.inputtext[id=email]").send_keys("this is tag ,classs and attribute")




# l=d.find_elements(By.CLASS_NAME,"inputtext")
# print(len(l))
# x=d.find_elements(By.TAG_NAME,"input")
# print(len(x))
# d.find_element(By.PARTIAL_LINK_TEXT,"Forgotten").click()
# #d.find_element(By.LINK_TEXT,"Forgotten password?").click()
time.sleep(3)