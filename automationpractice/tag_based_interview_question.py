"""
1 Find total no. of links in amazon.com
2 Find total images in amazon.com and store in file
"""

"""
1 Solution 
"""
import sys, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

# driver.get('https://www.amazon.com/')
# driver.implicitly_wait(10)
# link_lists = driver.find_elements(By.TAG_NAME, 'a')
# print(len(link_lists))
# for link_list in link_lists:
#     print(link_list.text)
#     print(link_list.get_attribute('href'))


"""
2 Solution 
"""
driver.get('https://www.amazon.com/')
driver.implicitly_wait(10)
image_lists = driver.find_elements(By.TAG_NAME, 'a')
images = []
print(len(image_lists))
for image in image_lists:
    ele = image.text
    print(ele)
    print(image.get_attribute('href'))
    image_link = image.get_attribute('href')
    images.append(image_link)

print(images)
f = open('store_image_link.txt','w+')
for image in images:
    if image:
        f.write(image+'\n')
f.close()