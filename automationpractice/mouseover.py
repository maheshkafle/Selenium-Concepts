from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://book.spicejet.com/')
driver.maximize_window()
driver.implicitly_wait(5)

login_ele = driver.find_element(By.ID, "Login")
action_chain = ActionChains(driver)
driver.implicitly_wait(4)
action_chain.move_to_element(login_ele).perform()
spice_club_members_ele = driver.find_element(By.LINK_TEXT, "SpiceClub Members")
action_chain.move_to_element(spice_club_members_ele).perform()
member_login = driver.find_element(By.LINK_TEXT, "Member Login")
member_login.click()
# driver.quit()