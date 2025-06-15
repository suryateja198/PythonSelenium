from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
s=Service(r"C:\pythondrivers\msedgedriver.exe")
d=webdriver.Edge(service=s)

d.get("https://www.facebook.com/")
time.sleep(1)


d.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input").send_keys("bYE")
time.sleep(2)
d.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/input[1]").clear()

time.sleep(4)

# #  to find the no elements with same name
# inpu =d.find_elements(By.TAG_NAME,"input")
# cla=d.find_elements(By.CLASS_NAME,"inputtext")
#
# print(len(inpu), len(cla))
#







# d.find_element(By.NAME,"email").send_keys("mymail.com")
# d.find_element(By.ID,"pass").send_keys("password")
# lis = d.find_elements(By.TAG_NAME,"div")
# print(len(lis))
# #d.find_element(By.PARTIAL_LINK_TEXT,"Forgotten password?").click()
# # d.find_element(By.LINK_TEXT,"Forgotten password?").click()
# # time.sleep(5)