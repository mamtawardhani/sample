from selenium import webdriver

import time
startUrl = "https://www.google.com"
browser = webdriver.Chrome("./chromedriver.exe")


browser.get(startUrl)

time.sleep(20000)