import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)

# Authentication popup username:password@web-address
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()
time.sleep(3)




time.sleep(3)
driver.quit()
