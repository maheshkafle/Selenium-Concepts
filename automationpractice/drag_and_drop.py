from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://demoqa.com/droppable')
driver.maximize_window()
driver.implicitly_wait(5)

source = driver.find_element(By.ID, 'draggable')
target = driver.find_element(By.ID, 'droppable')
action_chain = ActionChains(driver)
action_chain.drag_and_drop(source,target).perform()