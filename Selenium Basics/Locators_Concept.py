from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
base_url = driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/?")
driver.maximize_window()
print(driver.title)

username_url = driver.find_element(By.ID, "Form_submitForm_subdomain")
fullname = driver.find_element(By.ID, "Form_submitForm_Name")
email = driver.find_element(By.ID, "Form_submitForm_Email")
phone = driver.find_element(By.ID, "Form_submitForm_Contact")
country = driver.find_elements(By.ID, "Form_submitForm_Country")
contact_sale = driver.find_element(By.XPATH, "//a[contains(text(),'Contact Sales')]")
header_element = driver.find_elements(By.TAG_NAME, "a")

username_url.send_keys("JIJ's Automation Labs")
fullname.send_keys("Mohammad Jahidul Islam")
email.send_keys("jahidulij11@gmail.com")
phone.send_keys("6478711541")
# for c in country:
#     if c.text == "Canada":
#         c.click()
print(contact_sale.text)
print(len(header_element))
contact_sale.click()



time.sleep(4)
driver.quit()
