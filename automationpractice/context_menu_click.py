import sys, os
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')
driver.implicitly_wait(10)
action_chain = ActionChains(driver)
context_click_ele  = driver.find_element(By.XPATH, '/html/body/div/section/div/div/div/p/span')
action_chain.context_click(context_click_ele).perform()
items = driver.find_elements(By.CSS_SELECTOR, 'li.context-menu-item span')
for ele in items:
    print(ele.text)
    if ele.text == 'Copy':
        break
# driver.implicitly_wait(5)
# driver.quit()