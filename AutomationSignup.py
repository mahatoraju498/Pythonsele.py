from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
# from AccountINFO import AccountI
# from Addressinfo import AddressINFO




driver=webdriver.Chrome()
driver.get("https://automationexercise.com/")

time.sleep(4)
# driver.maximize_window()
# signup=driver.find_element(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')
# signup.click()

# #new user signup 
# Newuser= driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[3]/div/form/input[2]')
# Username=input("enter the name")

# Newuser.clear()
# Newuser.send_keys(Username)
# Newuser.send_keys(Keys.RETURN)

# #for email id 
# Useremail = driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[3]/div/form/input[3]')
# email =input("enter you email")
# Useremail.clear()
# Useremail.send_keys(email)
# Useremail.send_keys(Keys.RETURN)

# #submit button
# # submit_btn = WebDriverWait(driver,19).until(
# #     EC.element_to_be_clickable((By.XPATH,'//*[@id="form"]/div/div/div[3]/div/form/button'))
# # )
# # driver.execute_script("arguments[0].scrollIntoView();", submit_btn)
# # submit_btn.click()
# # time.sleep(5)

# account = AccountI();

# #enter account information
# Mr_radio_btn = WebDriverWait(driver,5).until(
#     EC.element_to_be_clickable((By.XPATH,'//*[@id="id_gender1"]'))

# )
# #NRs button clikable
# Mrs_radio_btn =WebDriverWait(driver,5).until(
#     EC.element_to_be_clickable((By.XPATH,'//*[@id="id_gender2"]'))
# )

# time.sleep(6)

# if(account.gender)=="Mr.":
#     Mr_radio_btn.click()
# elif(account.gender)=="Mrs.":
#     Mrs_radio_btn.click()
# time.sleep(5)

# # name_field=driver.find_element(By.XPATH,'//*[@id="name"]')
# # name_field.send_keys(account.name)
# pass_field=driver.find_element(By.XPATH,'//*[@id="password"]')
# pass_field.send_keys(account.password)
# time.sleep(8)


# account = AccountI();
# #DOB assign
# Date_birth = input("enter your DOB")
# day,month,year = Date_birth.split(' ')

# day_dropdown = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.NAME, "days")))  
# Select(day_dropdown).select_by_value(day) 
# time.sleep(8)

# month_dropdown = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.NAME, "months")))  
# Select(month_dropdown).select_by_value(month) 
# time.sleep(5)
# year_dropdown = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.NAME, "years")))  
# Select(year_dropdown).select_by_value(year) 
# time.sleep(5)


# #check box selection
# checkbox1=driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div/div[1]/form/div[6]/label')
# checkbox2=driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div/div[1]/form/div[7]/label')

# if(account.check)=="newletter":
#     checkbox1.click()
# elif(account.check)=="offer":
#     checkbox2.click()
# elif(account.check)=="both":
#     if not checkbox1.is_selected():
#         checkbox1.click()
#     if not checkbox2.is_selected():
#         checkbox2.click()
# elif(account.check)=="none":
#     print("no check box is selected:")
# else:
#     print("invalid choice,please enter 1,2,3,")
# time.sleep(10)


# #Address information part
# Information=AddressINFO();

# Firstname= driver.find_element(By.XPATH,'//*[@id="first_name"]')
# Firstname.send_keys(Information.firstname)
# time.sleep(3)
# Lastname
