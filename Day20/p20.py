import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s=Service("C:\pythondrivers\chromedriver-win64\chromedriver.exe")
d=webdriver.Chrome(service=s)
d.implicitly_wait(10)
d.get("https://text-compare.com/")
d.maximize_window()
a=d.find_element(By.ID,"inputText1")
b=d.find_element(By.ID,"inputText2")
a.send_keys("welcome")
act=ActionChains(d)
act.key_down(Keys.CONTROL)
act.send_keys('a')
act.key_up(Keys.CONTROL)
act.perform()
act.key_down(Keys.CONTROL)
act.send_keys("c")
act.key_up(Keys.CONTROL)
act.perform()
act.send_keys(Keys.TAB).perform()
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
import time
time.sleep(10)
