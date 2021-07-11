from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

browserName = "chrome"

if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
else:
    print("Please pass the correct browser name:" + browserName)

driver.implicitly_wait(5)
# driver.get('http://google.com')
driver.find_element(By.NAME,'q').send_keys('mahesh kafle' + Keys.ENTER)
time.sleep(4)
driver.quit()
