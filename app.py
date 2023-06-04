from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
page = 'https://in.indeed.com/jobs?q=data+engineer&l=india'
driver.get(page)

element = driver.find_elements(By.XPATH, "/html/body/main/div[@id='jobsearch-Main']/div[@id='jobsearch-JapanPage']/div/div[@class='jobsearch-JapanPageLayout jobsearch-JapanSerpContainer is-i18n']/div[@class='jobsearch-SerpMainContent ']/div[@class='jobsearch-LeftPane']/div[5]/div[1]/ul[1]/li")
for e in element:
    try:
        cmp = e.find_element(By.CLASS_NAME, "companyName")
        print(cmp.text)
        loc = e.find_element(By.CLASS_NAME, "companyLocation")
        print(loc.text)
        print()
    except:
        pass
