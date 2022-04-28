import xlrd
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/?")
url_info = driver.find_element(By.ID, "Form_submitForm_subdomain")
full_name = driver.find_element(By.ID, "Form_submitForm_Name")
email_id = driver.find_element(By.ID, "Form_submitForm_Email")
phone_no = driver.find_element(By.ID, "Form_submitForm_Contact")
country_name = driver.find_element(By.ID, "Form_submitForm_Country")
# captcha = driver.find_element(By.XPATH, '//*[@id="recaptcha-anchor"]')


workbook = xlrd.open_workbook("TestData.xls")
sheet = workbook.sheet_by_name("signup")
# Rows & Columns count
rowCount = sheet.nrows
columnCount = sheet.ncols

for row in range(1, rowCount):
    url = sheet.cell_value(row, 0)
    fullname = sheet.cell_value(row, 1)
    email = sheet.cell_value(row, 2)
    phone = sheet.cell_value(row, 3)
    country = sheet.cell_value(row, 4)

    # print(str(url) + str(fullname) + str(email) + str(phone) + str(country))

    url_info.clear()
    url_info.send_keys(url)
    full_name.clear()
    full_name.send_keys(fullname)
    email_id.clear()
    email_id.send_keys(email)
    phone_no.clear()
    phone_no.send_keys(phone)
    # country_name.clear()
    country_name.send_keys(country)

    time.sleep(4)
