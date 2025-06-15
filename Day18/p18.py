# EPSIODE 8 practicing

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service(r"C:\pythondrivers\chromedriver-win64\chromedriver.exe")
d=webdriver.Chrome(service=s)
d.get("https://testautomationpractice.blogspot.com/")
d.implicitly_wait(10)
d.maximize_window()
d.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("Selenium")
d.find_element(By.XPATH,"//input[@type='submit']").click()

lis=d.find_elements(By.XPATH,"//div[@id='Wikipedia1_wikipedia-search-results']//div//a")
for i in lis:
    i.click()
time.sleep(2)
print(d.current_window_handle)
e=d.window_handles
print(len(e))
for i in e:
    d.switch_to.window(i)
    print(d.title)
    if d.title == "Selenium in biology - Wikipedia":
        time.sleep(10)

# input("Press Enter to close browser manually...")


