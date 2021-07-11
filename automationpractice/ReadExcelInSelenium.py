import time

import xlrd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.orangehrm.com/orangehrm-30-day-trial/')

url = driver.find_element(By.ID, 'Form_submitForm_subdomain')
first_name = driver.find_element(By.ID, 'Form_submitForm_FirstName')
last_name = driver.find_element(By.ID, 'Form_submitForm_LastName')
email = driver.find_element(By.ID, 'Form_submitForm_Email')
job_title = driver.find_element(By.ID, 'Form_submitForm_JobTitle')
company_name = driver.find_element(By.ID, 'Form_submitForm_CompanyName')
contact = driver.find_element(By.ID, 'Form_submitForm_Contact')
total_employee = driver.find_element(By.ID, 'Form_submitForm_NoOfEmployees')
industry = driver.find_element(By.ID, 'Form_submitForm_Industry')
country = driver.find_element(By.ID, 'Form_submitForm_Country')



workbook = xlrd.open_workbook("DataSource.xlsx")
sheet = workbook.sheet_by_name("MockData")

# get total no. of rows
row_count = sheet.nrows
column_count = sheet.ncols
print(row_count)
print(column_count)

for row in range(1, row_count):
    url_value = sheet.cell_value(row, 0)# '0' means it reads value from 1 column
    first_name_value = sheet.cell_value(row, 1) # '1' means it reads value from 1 column
    last_name_value = sheet.cell_value(row, 2)
    email_value = sheet.cell_value(row, 3)
    job_title_value = sheet.cell_value(row, 4)
    company_name_value = sheet.cell_value(row, 5)
    contact_value = sheet.cell_value(row, 6)
    total_employee_value = sheet.cell_value(row, 7)
    industry_value = sheet.cell_value(row, 8)
    country_value = sheet.cell_value(row, 9)

    url.clear()
    url.send_keys(url_value)
    first_name.clear()
    first_name.send_keys(first_name_value)
    last_name.clear()
    last_name.send_keys(last_name_value)
    email.clear()
    email.send_keys(email_value)
    job_title.clear()
    job_title.send_keys(job_title_value)
    company_name.clear()
    company_name.send_keys(company_name_value)
    contact.clear()
    contact.send_keys(contact_value)
    # total_employee.clear()
    # total_employee.send_keys(total_employee_value)
    # industry.clear()
    # industry.send_keys(industry_value)
    # country.clear()
    # country.send_keys(country_value)
    time.sleep(3)