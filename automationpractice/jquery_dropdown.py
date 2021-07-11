from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/')
driver.implicitly_wait(5)

def select_jquery_dropdown_values(ID, css_selector):
    show_dropdown_list = driver.find_element(By.ID, ID)
    show_dropdown_list.click()
    dropdown_values = driver.find_elements(By.CSS_SELECTOR, css_selector)
    for ele in dropdown_values:
     print(ele.text)
     if ele.text == 'choice 6 2 3':
        ele.click()
        break

select_jquery_dropdown_values('justAnInputBox', 'span.comboTreeItemTitle')
driver.refresh()
driver.implicitly_wait(10)
select_jquery_dropdown_values('justAnInputBox1', 'span.comboTreeItemTitle')
driver.refresh()
driver.implicitly_wait(10)
select_jquery_dropdown_values('justAnotherInputBox', 'span.comboTreeItemTitle')