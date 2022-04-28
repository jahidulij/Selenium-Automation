from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
base_url = driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
driver.maximize_window()
print(driver.title)

# countries = driver.find_element(By.ID, 'Form_submitForm_Country')
# select = Select(countries)
# select.select_by_visible_text('Canada')
# select.select_by_index(17)
# select.select_by_value('United States')
# print(select.is_multiple)
# optionList = select.options
def select_values_from_dropdown(dropDownOptionsList, value):
    print(len(dropDownOptionsList))
    for option in dropDownOptionsList:
        print(option.text)
        if option.text == value:
            option.click()
            break

countryList = driver.find_elements(By.XPATH, '//select[@id=\'Form_submitForm_Country\']/option')
select_values_from_dropdown(countryList, 'Germany')


time.sleep(3)
driver.quit()
