import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)

base_url = driver.get("https://www.amazon.ca/")
driver.maximize_window()
time.sleep(3)

driver.find_element(By.XPATH, '//*[@id="nav-xshop"]/a[1]').click()

driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.back()
time.sleep(2)
driver.refresh()
time.sleep(2)

time.sleep(3)
driver.quit()
