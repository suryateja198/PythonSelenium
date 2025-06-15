import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
s=Service(r"C:\pythondrivers\chromedriver-win64\chromedriver.exe")
d=webdriver.Chrome(service=s)
# # d.implicitly_wait(10)
d.get("https://www.facebook.com/")
# w=WebDriverWait(d,10,ignored_exceptions=(TimeoutException,))
# h=w.until(EC.presence_of_element_located((By.XPATH,"//input[@id='email']")))
# h.send_keys("surya")
#
# i=w.until(EC.presence_of_element_located((By.XPATH,"//input[@id='emai']")),None)
# if i:
#     i.send_keys("ravi")
# else:
#     print("element not available")
#
#
# j=w.until(EC.presence_of_element_located((By.XPATH,"//input[@id='email' and @name='email']")))
# j.send_keys("and operator good")
#
# # time.sleep(10)
#


w = WebDriverWait(d, 10, ignored_exceptions=(TimeoutException,))
element = w.until(EC.presence_of_element_located((By.XPATH, "//input[@id='emai']")), None)

if element:
    element.send_keys("test@example.com")
else:
    print("Element not found within the time limit.")