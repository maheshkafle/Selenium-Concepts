from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://the-internet.herokuapp.com/javascript_alerts')
driver.implicitly_wait(10)
ele = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/button')
ele.click()
time.sleep(3)
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
# alert.dismiss()
time.sleep(3)
driver.quit()
