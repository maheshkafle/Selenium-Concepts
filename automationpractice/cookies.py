from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get('https://www.reddit.com/')
cookies1 = driver.get_cookies()
for cookie in cookies1:
    print(cookie)
driver.add_cookie({"name":"mahesh","domain":"mahesh.com","value":"python"})
cookies2 = driver.get_cookies()
for cookie in cookies2:
    print(cookie)
driver.implicitly_wait(5)
driver.quit()