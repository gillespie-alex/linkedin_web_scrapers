from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import copy
from copy import deepcopy

import matplotlib.pyplot as plt

# LinkedIn credentials
email = 'smhlmfaololxdxd@gmail.com'
password = 'I_hate_networking_so_I_mad_a_bot_do_it'

position = 'culture war marine'
local = 'CHAZ'
position = position.replace(' ', "%20")
local = local.replace(' ', "%20")

# Open the LinkedIn browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.set_window_size(1024, 600)
driver.maximize_window()
driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
time.sleep(2)

# Now search for the credential inputs
driver.find_element(By.ID, 'username').send_keys(email)
driver.find_element(By.ID, 'password').send_keys(password)
driver.find_element(By.ID, 'password').send_keys(Keys.RETURN)

driver.get(f"https://www.linkedin.com/jobs/search/?currentJobId=3261433012&f_TPR=r604800&geoId=103644278&keywords={position}&location={local}&refresh=true")

time.sleep(2)

job_descriptions = []
company_links = []

# Job searches will be at max 40 pages, so loop through and click on each page
for i in range(1, 40):
    try:
        driver.find_element(By.XPATH, f'//button[@aria-label="Page {i}"][@type="button"]').click()
    except:
        # If this condition is reached it means there was not 40 pages to search
        break
    
    time.sleep(1.5) 

    # First find the jobs block
    job_list = driver.find_element(By.CLASS_NAME, f'scaffold-layout__list-container')

    # Then find all the job entries within the block
    jobs = job_list.find_elements(By.CLASS_NAME, 'jobs-search-results__list-item')

    # Now iterate through all the jobs as 'find_elements' returns a list of jobs
    for j in range(1, len(jobs) + 1):
        driver.find_element(By.XPATH, f"//ul[@class='scaffold-layout__list-container']/li[{j}]").click()

        time.sleep(1.5)

        description = driver.find_element(By.CLASS_NAME, f"jobs-description__container")
        company = driver.find_element(By.XPATH, f"//span[@class='jobs-unified-top-card__company-name']/a[1]")

        soup = BeautifulSoup(description.get_attribute('outerHTML'), 'lxml')
        soup2 = BeautifulSoup(company.get_attribute('outerHTML'), 'lxml')
        if job_descriptions and soup.text == job_descriptions[-1]:
            # if there are repeat job entries ignore them 
            continue
        job_descriptions.append(soup.text)

        # Now we want to get the link to their webpage from the company name 
        link = soup2.find(href=True)
        path = link['href']
        path = 'https://www.linkedin.com' + path[:-5]
        company_links.append(path)

# Navigating to each of the companies' webpages to find technical recruiters
used = set()
employee_search = "technical recruiter"
recruiters_links = [[] for _ in range(len(company_links))]
for i, link in enumerate(company_links):
    if link in used:
        continue
    used.add(link)
    driver.get(f"{link}")
    time.sleep(1)
    try:
        driver.find_element(By.XPATH, f"//div[@class='mt1']/div/a[2]").click()
    except:
        driver.find_element(By.XPATH, f"//div[@class='mt1']/div/a[1]").click()

    time.sleep(2)
    
    driver.find_element(By.XPATH, f"//input[@class='search-global-typeahead__input always-show-placeholder']").send_keys(employee_search)

    time.sleep(0.5)

    driver.find_element(By.XPATH, f"//input[@class='search-global-typeahead__input always-show-placeholder']").send_keys(Keys.RETURN)

    time.sleep(1)

    try:
        ppl_list = driver.find_element(By.XPATH, f"//ul[@class='reusable-search__entity-result-list list-style-none']")
    except:
        continue

    persons = ppl_list.find_elements(By.CLASS_NAME, f'reusable-search__result-container ')

    for k in range(1, len(persons) + 1):
        person = driver.find_element(By.XPATH, f"//ul[@class='reusable-search__entity-result-list list-style-none']/li[{k}]")
        profile = person.find_element(By.CLASS_NAME, f'app-aware-link')

        soup = BeautifulSoup(profile.get_attribute('outerHTML'), 'lxml')
        profile_href = soup.find(href=True)
        profile_path = profile_href['href']
        for c, char in enumerate(profile_path):
            if char == '?':
                profile_path = profile_path[:c]
                break
        recruiters_links[i].append(profile_path)

tech_recruiters = []
for array in recruiters_links:
    temp = ','.join(array)
    tech_recruiters.append(temp)

# Create pandas dataframe
df = pd.DataFrame(list(zip(company_links, job_descriptions, tech_recruiters)),
       columns = ['company_links', 'descriptions', 'tech_recruiters'])

# Ouput dataframe to .csv file if one wants to open in excel
t = time.time()
export_path = f'{int(t)}.csv'
df.to_csv(export_path)
