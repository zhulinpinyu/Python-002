from selenium import webdriver

import time, os

chrome = webdriver.Chrome()
chrome.get("https://shimo.im/login")
time.sleep(3)
chrome.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys(os.getenv('EMAIL'))
time.sleep(3)
chrome.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys(os.getenv('PASSWORD'))
time.sleep(3)
login_btn = chrome.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button')
login_btn.click()
print(chrome.get_cookies())
time.sleep(5)
chrome.close()