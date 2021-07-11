from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://the-internet.herokuapp.com/login')
driver.maximize_window()

wait = WebDriverWait(driver, 20)
wait.until(ec.title_contains('Internet'))
print(driver.title)
email_id = wait.until(ec.presence_of_element_located((By.ID,'username')))
email_id.send_keys('tomsmith')
password = driver.find_element(By.ID,'password')
password.send_keys('SuperSecretPassword!')
login = driver.find_element(By.CLASS_NAME,'radius')
login.click()
