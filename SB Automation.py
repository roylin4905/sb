from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome('C:/Users/Roylin Francis/OneDrive/Desktop/chromedriver.exe')
driver.get('https://skoolbeep-qa.2base.in/')
driver.maximize_window()
time.sleep(5)
login = driver.find_element(By.XPATH, '/html/body/div[2]/header/div/div/nav/ul/li[7]/a').click()
time.sleep(5)
login1 = driver.find_element(By.ID, 'user_mobile').send_keys('9495653799')
submitbutton = driver.find_element(By.XPATH, '/html/body/div[2]/section/div[1]/div/div[2]/div/form[1]/div[2]/div[3]/button').click()
time.sleep(5)
password = driver.find_element(By.ID, 'user_otp').send_keys('123456')
loginbutton = driver.find_element(By.XPATH, '/html/body/div[2]/section/div[1]/div/div[2]/div/form[2]/div[2]/div[5]/button').click()
time.sleep(5)
logoutbutton = driver.find_element(By.ID, 'header_tiny_profile_pic').click()
time.sleep(1)
logoutbutton = driver.find_element(By.XPATH, '/html/body/header/div[2]/nav/div[2]/ul[2]/li[3]/ul/div/div[2]/div/div/div[2]/a').click()
time.sleep(5)