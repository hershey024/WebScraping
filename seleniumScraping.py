from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pandas as pd
import time


website = 'https://www.adamchoi.co.uk/overs/detailed'
#path = 'C:/Users/harsh/Downloads/chrome-win64/chrome-win64/chrome'
s = webdriver.ChromeService(executable_path=r'C:\Users\harsh\Downloads\chromedriver-win64/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get(website)
# all_matches_button = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
# all_matches_button.click()


# Select stats by Country
dropdown = Select(driver.find_element(By.ID, 'country'))
dropdown.select_by_visible_text('Spain')

time.sleep(3)

date = []
home_team = []
score = []
away_team = []

matches = driver.find_elements(By.TAG_NAME, 'tr')
for match in matches:
    date.append(match.find_element(By.XPATH, './td[1]').text)
    home_team.append(match.find_element(By.XPATH, './td[2]').text)
    score.append(match.find_element(By.XPATH, './td[3]').text)
    away_team.append(match.find_element(By.XPATH, './td[4]').text)
    #print(match.text)

# print(date)
# print(home_team)
# print(score)
# print(away_team)

df = pd.DataFrame({'date' : date, 'home_team' : home_team, 'score' : score, 'away_team' : away_team})
df.to_csv('football_data.csv', index=False)
#driver.quit()