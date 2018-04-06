from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\\Users\\Thiago\\Desktop\\chromedriver.exe")
driver.get('https://web.whatsapp.com/')
time.sleep(5)
elements = driver.find_element_by_xpath('//*[@id="pane-side"]/div/div/div/div[1]/div/div/div[2]')
elements.click()
time.sleep(1)
while(True):
    elements = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    elements.send_keys("Oi, eu sou um bot")
    elements = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/button/span')
    elements.click()
