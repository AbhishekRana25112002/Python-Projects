from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#path of our chrome driver(a bridge between browser and selenuim
chrome_driver_path="C:\Development\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/")

#Signing in to linked in using bot
sign_in=driver.find_element(By.LINK_TEXT,"Sign in")
time.sleep(1)
sign_in.click()
username=driver.find_element(By.ID,"username")
username.send_keys("abhishekrana25112002@gmail.com")
password=driver.find_element(By.ID,"password")
password.send_keys("Abhi7037632200##")
sign_in2=driver.find_element(By.CLASS_NAME,"login__form_action_container")
time.sleep(1)
sign_in2.click()
time.sleep(1)

#searching for a link named fresher
job1=driver.find_element(By.LINK_TEXT,"Fresher")
job1.click()
time.sleep(5)

#Trying to apply for the job using bot click but some problem occuring, come back it to later
apply=driver.find_element(By.CLASS_NAME,"artdeco-button__text")
time.sleep(5)
apply.click()
