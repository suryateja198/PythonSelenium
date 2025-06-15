#class 1&2
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

S=Service(r"C:\pythondrivers\chromedriver-win64\chromedriver.exe")
d=webdriver.Chrome(service=S)

d.get("https://www.qa-practice.com/elements/select/single_select")
a=d.find_element(By.XPATH,"//select[@id='id_choose_language']")
b=Select(a)
print(help(Select))
# b.select_by_visible_text('Python')
# time.sleep(3)
# d.get("https://www.qa-practice.com/elements/checkbox/mult_checkbox")
# a=d.find_elements(By.XPATH,"//li[@class='active']/ancestor::*")
# for i in a:
#     print(i.text)



# a=d.find_elements(By.CLASS_NAME,"form-check-input")
# print(len(a))
# for i in a:
#     i.click()
#     print(i.text)


# d.get("https://www.facebook.com/")
# print(d.title)
# print(d.current_url)
# print(d.page_source)
# d.get("https://www.amazon.in/")
# print(d.title)
# print(d.current_url)
# d.back()
# d.forward()
# d.back()
# d.find_element(By.PARTIAL_LINK_TEXT,"For").click()
# d.refresh()
# a=d.find_elements(By.CLASS_NAME,"inputtext")
# print(len(a))
# for i in a:
#     print(i.text)
#     print(i.get_attribute('id'))
# d.find_element(By.ID,"email").send_keys("hi@")
# time.sleep(3)
# d.find_element(By.NAME, "email").clear()
# time.sleep(2)
# a=d.find_element(By.CSS_SELECTOR,"#email")
# if a.is_enabled():
#     a.send_keys("this is css_selector")
# time.sleep(3)
# d.find_element(By.CSS_SELECTOR,".inputtext").send_keys("this is css_selector")
# time.sleep(3)
# d.find_element(By.CSS_SELECTOR,"input[data-testid=royal-email]").send_keys("hello")
# d.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal-pass]").send_keys("bye")
time.sleep(3)
d.quit()