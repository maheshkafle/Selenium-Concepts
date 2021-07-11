import sys, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.orangehrm.com/orangehrm-30-day-trial/')
driver.implicitly_wait(10)
country_list = []
industry_list = []

def select_dropdown_by_id(ID,text_value):
    select = driver.find_element(By.ID, ID)
    select_option= Select(select)
    select_option.select_by_value(text_value)
    select_option.select_by_visible_text(text_value)

def select_dropdown_by_XPATH(XPATH, list):
    select = driver.find_elements(By.XPATH, XPATH)
    for ele in select:
          if ele.text:
              print(ele.text)
              list.append(ele.text)

print(list)

# Select By ID
# select_dropdown_by_id('Education','Form_submitForm_Industry')
# select_dropdown_by_id('Australia', 'Form_submitForm_Country')

# Select By XPATH
select_dropdown_by_XPATH('//*[@id="Form_submitForm_Country"]', country_list)
print(country_list)
select_dropdown_by_XPATH('//*[@id="Form_submitForm_Industry"]', industry_list)
print(industry_list)

country_list_file = open('country_list.txt', 'w+')
industry_list_file = open('industry_list.txt', 'w+')

for country in country_list:
    if country:
        country_list_file.write(country + '\n')

country_list_file.close()

for industry in industry_list:
    if industry:
        industry_list_file.write(industry + '\n')

industry_list_file.close()
driver.quit()

