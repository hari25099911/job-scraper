from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
service_obj = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)
# driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)

print()
print("<<......Job-Scraper......>>")
print()
job_role = 'dataengineer' #str(input('enter job role: '))
lst = job_role.split(' ')
str = ""
c = 0
for i in lst:
    i = i.strip()
    if c == 0:  
        str+=i
        c+=1
    else:
        str+='+'+i
        c+=1
page = f'https://www.foundit.in/srp/results?query="{str}"'
driver.get(page)
count = 0
print()
print('starting to scrape............. ')
print()
while count < 1000:
    elements = driver.find_elements(By.XPATH, "/html/body/div[@id='srpThemeDefault']/div[@class='srpContainer']/div[@id='srpContent']/div[@class='srpCardContainer']/div[@class='srpResultCard']/div")
    for element in elements:
        try:
            job_title = element.find_element(By.CLASS_NAME, "jobTitle").text
            company_name = element.find_element(By.CLASS_NAME, "companyName").text
            skills = [i.text for i in element.find_elements(By.CLASS_NAME, "skillTitle")]
            while("" in skills):
                skills.remove("")
            sub_element = element.find_element(By.CLASS_NAME, "cardBody")
            job_type = sub_element.find_element(By.XPATH, "div[1]/div[@class='details']").text
            location = sub_element.find_element(By.XPATH, "div[2]/div[@class='details']").text   
            print(job_title, company_name, skills, job_type, location)
            count += 1
        except:
            pass
    try:
        element.find_element(By.CLASS_NAME, "mqfisrp-right-arrow").click()
        print()
        print("Navigating to Next Page") 
        print()
    except :
        print()
        print("Reached Last Page")
        print()
        break
driver.quit()
print('count:',count)
print()
print('scraping ends............. ')
print()
