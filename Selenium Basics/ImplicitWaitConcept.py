import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
# timeout = 10
# dynamic wait
# implicitly wait will be applied for every web elements
# global wait
# find element
# find elements
# only for web elements
# not for non web elements like: title, url, alerts

driver.get("https://app.hubspot.com/")
driver.maximize_window()
username = driver.find_element(By.ID, "username")
username.send_keys("abc@mail.com")
driver.implicitly_wait(5)
password = driver.find_element(By.ID, "password")
password.send_keys("test123")
driver.implicitly_wait(0)
