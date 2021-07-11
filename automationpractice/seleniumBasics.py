from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# driver = webdriver.Chrome('C:\\Commit Projects\\seleniumprojects\\drivers\\chromedriver_win32\\chromedriver.exe')
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
# driver.get('http://google.com')
assert "Google" in driver.title
search_box = driver.find_element(By.NAME, 'q').send_keys('pycharm')
option_list = driver.find_elements(By.CSS_SELECTOR, 'ul.erkvQe li span')
print(len(option_list))

for ele in option_list:
    print(ele.text)
    if ele.text == 'pycharm download':
        ele.click()
        break

time.sleep(5)
driver.quit()
