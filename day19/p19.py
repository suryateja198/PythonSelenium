# episode 11 practcing
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


s=Service(r"C:\pythondrivers\chromedriver-win64\chromedriver.exe")
d=webdriver.Chrome(service=s)
d.implicitly_wait(10)
d.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
d.maximize_window()
d.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
d.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
d.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
# d.find_element(By.XPATH,"//a[@class='oxd-main-menu-item active']").click()
# d.find_element(By.XPATH,"//span[normalize-space()='User Management']").click()
time.sleep(10)

wait = WebDriverWait(d, 20)
admin_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[1]//a[1]//span[1]")))
admin_menu.click()

# wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='User Management']"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Job']"))).click()
time.sleep(10)
JobTitles=d.find_element(By.XPATH,"//a[normalize-space()='Job Titles']")
PayGrades=d.find_element(By.XPATH,"//a[normalize-space()='Pay Grades']")
emplyStatus=d.find_element(By.XPATH,"//a[normalize-space()='Employment Status']")
workshifts=d.find_element(By.XPATH,"//a[normalize-space()='Work Shifts']")

a=ActionChains(d)
# a.move_to_element(JobTitles).move_to_element(PayGrades).move_to_element(emplyStatus).move_to_element(workshifts).click().perform()

a.context_click(JobTitles).perform()
a.double_click()
time.sleep(10)
d.quit()