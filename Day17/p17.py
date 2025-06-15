
# Episode 9 practice

# Auto popup alert
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
s=Service(r"C:\pythondrivers\chromedriver-win64\chromedriver.exe")
d=webdriver.Chrome(service=s,options=ops)

# d.get("https://whatmylocation.com/")
# time.sleep(4)

d.get("https://testautomationpractice.blogspot.com/")
# time.sleep(4)

# get the number of rows and columns for a table
row=len(d.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr"))
col=len(d.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr/th"))
print("the number of rows",row)
print("the number of cols",col)

#get the specified element
# e=d.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[3]/td[3]").text
# print("the specified element",e)

# get all the rows & colums data
# for i in range(2,row+1):
#     for j in range(1,col+1):
#         # f=d.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(i)+"]/td["+str(j)+"]").text
#         f = d.find_element(By.XPATH, f"//table[@name='BookTable']/tbody/tr[{i}]/td[{j}]").text
#         print(f,end=" ")
#     print(" ")

# get specified with specific conditon

for i in range(2,row+1):
    autor = d.find_element(By.XPATH, f"//table[@name='BookTable']/tbody/tr[{i}]/td[2]").text
    if autor=="Amod":
        book_name=d.find_element(By.XPATH, f"//table[@name='BookTable']/tbody/tr[{i}]/td[1]").text
        price = d.find_element(By.XPATH, f"//table[@name='BookTable']/tbody/tr[{i}]/td[4]").text
        print(book_name+"  "+price)


