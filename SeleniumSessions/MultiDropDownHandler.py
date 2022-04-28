from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
base_url = driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
driver.maximize_window()
print(driver.title)
time.sleep(2)

def select_values(optionList, value):
    if not value [0] == 'all':
        for element in drop_down_list:
            print(element.text)
            for k in range(len(value)):
                if element.text == value[k]:
                    element.click()
                    break
    else:
        try:
            for element in optionList:
                element.click()
        except Exception as e:
            print(e)

# Single Selection
# single_selector = driver.find_element(By.ID, 'justAnotherInputBox')

# Multi Selection
driver.find_element(By.ID, 'justAnInputBox').click()
time.sleep(3)
drop_down_list = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')
# select_values(drop_down_list, 'choice 3')
# select_values(drop_down_list, 'choice 6 2 1')
# Select specifics
# value_list = ['choice 2']
value_list = ['choice 2', 'choice 3', 'choice 6 2 1']
# All Select
# value_list = ['all']

select_values(drop_down_list, value_list)



# Multi Selection With Cascade Option Select






time.sleep(3)
driver.quit()
