from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://the-internet.herokuapp.com/upload')
driver.maximize_window()
driver.implicitly_wait(5)
file_upload = driver.find_element(By.NAME, 'file').send_keys('C:\\Users\\mahesh.kafle\\Desktop\\image.jpg')
# file_upload.send_keys('C:\Users\mahesh.kafle\Desktop\SMF\Slackadding_new_member.smf')
upload_btn = driver.find_element(By.ID, 'file-submit')
upload_btn.send_keys(Keys.ENTER)