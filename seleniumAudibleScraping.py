from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

options = Options()
options.headless = False
#options.add_argument('window-size=1920x1080')

website = 'https://www.audible.in/adblbestsellers'
#https://www.audible.in/adblbestsellers
#https://www.audible.com/search

s = webdriver.ChromeService(executable_path=r'C:\Users\harsh\Downloads\chromedriver-win64/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)
driver.get(website)
driver.maximize_window()

#pagination
pagination = driver.find_element(By.XPATH, '//ul[contains(@class, "pagingElements")]')
pages = pagination.find_elements(By.TAG_NAME, 'li')
last_page = int(pages[-2].text)

book_title = []
book_author = []
book_length = []

current_page = 1

while current_page <= 2:  #last_page:
    #time.sleep(2)
    container = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'adbl-impression-container ')))
    #container = driver.find_element(By.CLASS_NAME, 'adbl-impression-container ')
    #print(container)

    products = WebDriverWait(container, 5).until(EC.presence_of_all_elements_located((By.XPATH,'./div/span/ul/li')))
    #container.find_elements(By.XPATH, './div/span/ul/li')
    #products = container.find_elements(By.XPATH, './div/span/ul/li') # ./ -> current container context
    print(products)

    for product in products:
        book_title.append(product.find_element(By.XPATH, './/h3[contains(@class, "bc-heading")]').text)
        book_author.append(product.find_element(By.XPATH, './/li[contains(@class, "authorLabel")]').text)
        book_length.append(product.find_element(By.XPATH, './/li[contains(@class, "runtimeLabel")]').text)

    current_page += 1

    try:
        next_page = driver.find_element(By.XPATH, '//span[contains(@class, "nextButton")]')
        next_page.click()
    except:
        pass

driver.quit()
print(book_title)
df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length})
df_books.to_csv('books.csv', index=False)