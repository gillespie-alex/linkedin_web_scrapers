from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import copy
from copy import deepcopy

import matplotlib.pyplot as plt

# LinkedIn credentials
email = 'smtg@yahoo.com'
password = 'bots>humans'
message = f"Hello, I hope you are having a wonderful year so far. I need a job, I will do anything for a job, I'll even take negative wages for a job"

# Open the LinkedIn browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.set_window_size(1024, 600)
driver.maximize_window()
driver.get('https://www.linkedin.com/login')
time.sleep(2)

# Now search for the credential inputs
driver.find_element(By.ID, 'username').send_keys(email)
driver.find_element(By.ID, 'password').send_keys(password)
driver.find_element(By.ID, 'password').send_keys(Keys.RETURN)

time.sleep(2.5)

# Change this asterisk to the .csv created by 'linkedinscraper.py' file
df = pd.read_csv('./*.csv')
recruiters = df.iloc[:, -1]
for link in recruiters:
    if isinstance(link, float):
        continue
    List1 = link.split(',')
    for person in List1:
        driver.get(person)
        time.sleep(2)

        try:
            connect = driver.find_element(By.XPATH, f"//div[@class='pvs-profile-actions__action']/button[1]")
            time.sleep(1.5)
            driver.execute_script("arguments[0].click();", connect)
            time.sleep(1)
        except:
            print("this is a headless person")
            continue

        try:
            add_note = driver.find_element(By.XPATH, f"//button[@aria-label='Add a note']")
            driver.execute_script("arguments[0].click();", add_note)
            time.sleep(1.5)

            driver.find_element(By.ID, 'custom-message').send_keys(message)
            time.sleep(10)

            Send = driver.find_element(By.XPATH, f"//button[@aria-label='Send now']")
            driver.execute_script("arguments[0].click();", Send)
            time.sleep(2)
        except:
            # This person has already been contacted
            continue



