import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.maximize_window()
driver.get('https://www.facebook.com/')

email=driver.find_element_by_xpath('.//*[@id="email"]')
file = open("usr.txt")
content = file.readlines()
usr_lines = (content[0])
email.send_keys(usr_lines)

password=driver.find_element_by_xpath('.//*[@id="pass"]')
with open('pass.txt','r') as myfile:
    password1=myfile.read().replace('\n','')
password.send_keys(password1)

login=driver.find_element_by_class_name("_6ltg")
print("Logging in")
time.sleep(3)
login.click()
print("OK")

#Load Facebook then post on mbasic //sleep added in fear of szuucc detecting it as bot*maybe
time.sleep(5)
driver.get('https://mbasic.facebook.com/')

time.sleep(2)
print("Selecting statusbox")
statusbox=driver.find_element_by_xpath('//*[@id="mbasic-composer-form"]/table/tbody/tr/td[2]/div/textarea')
statusbox.click()
with open('lastword.txt') as f:
#     contents = f.read()
# email.send_keys(contents)
    lastwd=f.read().replace('\n','')
statusbox.send_keys(lastwd)
# statusbox.send_keys('Test from b o o o t t t ')

time.sleep(2)
print("Selecting POST")
postbox=driver.find_element_by_xpath('//*[@id="mbasic-composer-form"]/table/tbody/tr/td[3]/div/input')
postbox.click()

#logout logic
time.sleep(5)
logout=driver.find_element_by_xpath('//*[@id="header"]/nav/a[10]')
logout.click()
time.sleep(3)
logout=driver.find_element_by_xpath('//*[@id="mbasic_logout_button"]')
logout.click()
time.sleep(3)
driver.refresh()
logout=driver.find_element_by_xpath('//*[@id="root"]/table/tbody/tr/td/div/form[2]/input[3]')
time.sleep(3)
logout.click()

time.sleep(3)
driver.quit()
