import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
Ser=Service(r"C:\pythondrivers\msedgedriver.exe")
d=webdriver.Edge(service=Ser)
d.get("https://www.facebook.com/")
d.maximize_window()
time.sleep(3)
# d.find_element(By.CLASS_NAME,"inputtext").send_keys("chii")
d.find_element(By.NAME,"email").send_keys("heeloo")
d.find_element(By.ID,"pass").send_keys("bye")
time.sleep(3)
d.find_element(By.NAME,"email").clear()
d.find_element(By.CSS_SELECTOR,"#email").send_keys("hello")
time.sleep(3)
d.find_element(By.NAME,"login").click()
time.sleep(3)
print(d.title)



