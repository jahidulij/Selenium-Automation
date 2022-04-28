import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://app.hubspot.com/")
print(driver.title)
driver.maximize_window()
wait = WebDriverWait(driver, 10)
wait.until(ec.title_is('HubSpot Login'))
# wait.until(ec.title_contains('HubSopt'))
print(driver.title)
email_id = wait.until(ec.presence_of_element_located((By.ID, 'username')))
email_id.send_keys("test@mail.com")
password = driver.find_element(By.ID, "password").send_keys("test123")

time.sleep(3)
print(driver.title)
# username = driver.find_element(By.ID, "username")
# username.send_keys("abc@mail.com")
# password = driver.find_element(By.ID, "password")
# password.send_keys("test123")
