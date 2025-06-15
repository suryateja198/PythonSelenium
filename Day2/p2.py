import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
Ser=Service(r"C:\pythondrivers\msedgedriver.exe")
d=webdriver.Edge(service=Ser)
d.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
d.maximize_window()
time.sleep(3)
d.find_element(By.NAME,"username").clear()
d.find_element(By.CLASS_NAME,"yt-core-image yt-core-image--fill-parent-height yt-core-image--fill-parent-width yt-core-image--content-mode-scale-aspect-fill yt-core-image--loaded").click()