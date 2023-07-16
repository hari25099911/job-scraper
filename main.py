from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import streamlit as st

@st.experimental_singleton
def get_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--headless')
driver = get_driver()

print()
print("<<......Job-Scraper......>>")
print()
st.title('Trends in Data jobs')
job_role = st.selectbox('Select a job role?', ("Data Engineer", "Data Analyst", "Data Architect", "Data Scientist", "Machine Learning Engineer"))
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
# page = f'www.foundit.in/srp/results?query="{str}"'
page = page.encode('ascii', 'ignore').decode('unicode_escape')
driver.get(page)
count = 0
print()
print('starting to scrape............. ')
print()
while count < 50:
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
            st.write(job_title, company_name, skills, job_type, location)
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
