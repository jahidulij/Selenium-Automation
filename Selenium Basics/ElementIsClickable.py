import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://app.hubspot.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)
signup_link = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, "Sign up")))
print(signup_link.text)
signup_link.click()

first_name = wait.until(ec.visibility_of_element_located((By.ID, "UIFormControl-2")))
first_name.send_keys("test")

time.sleep(3)
print(driver.title)
