from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.google.com')
title = driver.title
print(title)
