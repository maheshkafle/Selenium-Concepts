from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# driver = webdriver.Chrome('C:\\Commit Projects\\seleniumprojects\\drivers\\chromedriver_win32\\chromedriver.exe')
driver = webdriver.Chrome(ChromeDriverManager().install())

# Form submission
driver.get('http://the-internet.herokuapp.com/')

# form_authentication = driver.find_element(By.PARTIAL_LINK_TEXT,'Form')
# form_authentication.click()

# username = driver.find_element(By.ID, 'username')
# password = driver.find_element(By.ID, 'password')
# login_btn = driver.find_element(By.CLASS_NAME, 'radius')

title_new = WebDriverWait(driver, 10).until(EC.title_contains("The Internet"))
print(driver.title)

# username.send_keys('tomsmith')
# password.send_keys('SuperSecretPassword!')
# login_btn.send_keys(Keys.ENTER)
#
# div = driver.find_element(By.CLASS_NAME,'flash.success')
#
# if div:
#     logout = driver.find_element(By.PARTIAL_LINK_TEXT, 'Logout')
#     logout.click()

driver.implicitly_wait(2)
driver.quit()
