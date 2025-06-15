from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
s = Service(r"C:\pythondrivers\chromedriver-win64\chromedriver.exe")
d = webdriver.Chrome(service=s)
d.implicitly_wait(100)

#failed
# d.get("https://www.google.com/")
# f=d.find_element(By.XPATH,"//textarea[@id='APjFqb']")
# f.send_keys("selenium")
# d.find_element(By.XPATH,"//button[text()='Stay signed out']").click()
# f.click()
# d.find_element(By.XPATH,"//h3[normalize-space()='Introduction To Selenium Automation Testing']").click()

time.sleep(4)

#application commands
# d.get("https://www.facebook.com/")
# print(d.title)
# print(d.current_url)
# print(d.page_source)
# time.sleep(3)


#name,id,tagname,classname,linktext,partiallinktext

# d.find_element(By.NAME,"email").send_keys("byeee")
# time.sleep(3)
# d.find_element(By.ID,"email").clear()
# time.sleep(2)
# d.find_element(By.CLASS_NAME,"inputtext").send_keys("hello")
# time.sleep(2)
# h=d.find_elements(By.TAG_NAME,"div")
# print(len(h))
# d.find_element(By.LINK_TEXT,"Forgotten password?").click()
# d.back()
# time.sleep(3)
# d.forward()
# time.sleep(3)
# d.refresh()
# time.sleep(3)
# d.find_element(By.PARTIAL_LINK_TEXT,"Forgotten").click()
# time.sleep(3)

#text and get_attribute
# e=d.find_element(By.XPATH,"//input[@id='identify_email']")
# print(e.text)
# print(e.get_attribute("id"))
# f=d.find_elements(By.XPATH,"//ul[@class='uiList localeSelectorList _2pid _509- _4ki _6-h _6-j _6-i']//a")
# print(len(f))
# for i in range(len(f)):
#    print(f[i].text)
# f=d.find_elements(By.XPATH,"//input[@id='email' or @name='ema']")
# print(len(f))
# f[0].send_keys("hellooo")
# time.sleep(3)
# d.find_element(By.XPATH,"//input[contains(@name,'email')]").send_keys("odk")
# d.find_element(By.XPATH,"//input[starts-with(@id,'ema')]").send_keys("odk")
# d.find_element(By.XPATH,"//a[text()='Forgotten password?']").click()
# time.sleep(3)

