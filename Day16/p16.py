import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s=Service(r"C:\pythondrivers\chromedriver-win64\chromedriver.exe")
d=webdriver.Chrome(service=s)
d.get("https://seleniumbase.io/demo_page")
a=Select(d.find_element(By.XPATH,"//select[@id='mySelect']"))
b=a.options
print((len(b)))
for i in b:
    print(i.text)
# a.select_by_visible_text("Set to 50%")
# time.sleep(5)
# a.select_by_index(3)
# time.sleep(5)























#checkboxes practice

# a=d.find_elements(By.XPATH,"//input[contains(@name,'checkBoxName')]")
# print(len(a))
# for i in a:
#     print(i.get_attribute("name"))
#     i.click()
# print(a.is_selected())
# a.click()
# print(a.is_selected())
# b=d.find_elements(By.XPATH,"//input[@id='radioButton1']")
# time.sleep(3)


