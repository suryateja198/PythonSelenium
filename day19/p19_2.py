from selenium import webdriver
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service(r"C:\pythondrivers\chromedriver-win64\chromedriver.exe")
d=webdriver.Chrome(service=s)
d.implicitly_wait(10)
d.get("https://testautomationpractice.blogspot.com/")
d.maximize_window()
# f1=d.find_element(By.ID,"field1")
# f1.clear()
# f1.send_keys("welcome")
# f2=d.find_element(By.XPATH,"//input[@id='field2']").clear()
# time.sleep(5)
# but=d.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")
# act=ActionChains(d)
# act.double_click(but).perform()
# time.sleep(5)


Home=d.find_element(By.LINK_TEXT,"Home")
UdemyCourses=d.find_element(By.LINK_TEXT,"Udemy Courses")
OnlineTrainings=d.find_element(By.LINK_TEXT,"Online Trainings")
act=ActionChains(d)
# act.move_to_element(Home).perform()
# time.sleep(2)
# act.move_to_element(UdemyCourses).perform()
# time.sleep(2)
# act.move_to_element(OnlineTrainings).perform()
# time.sleep(2)
# src=d.find_element(By.XPATH,"//p[normalize-space()='Drag me to my target']")
# des=d.find_element(By.XPATH,"//div[@id='droppable']")
# act.drag_and_drop(src,des).perform()

min=d.find_element(By.XPATH,"//div[@id='HTML7']//span[1]")
max=d.find_element(By.XPATH,"//div[@id='HTML7']//span[2]")
print(max.location)
time.sleep(10)
act.drag_and_drop_by_offset(max,-100,0).perform()
time.sleep(5)
print(max.location)

