from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s=Service(r"C:\pythondrivers\chromedriver-win64\chromedriver.exe")
d=webdriver.Chrome(service=s)
