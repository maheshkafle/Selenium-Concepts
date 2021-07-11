from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(10)
driver.get('https://www.reddit.com/')
driver.implicitly_wait(10)
'''
partial screenshot
'''
# driver.get_screenshot_as_file('reddit_1.png')

'''
Full Screenshot
You need to make sure that you are running in headless mode    
'''
screen = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(screen('Width'), screen('Height'))
driver.find_element_by_tag_name('body').screenshot('reddit_full_1.png')
driver.implicitly_wait(3)
driver.quit()