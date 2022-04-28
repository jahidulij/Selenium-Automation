import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)

# Authentication popup username:password@web-address
driver.get("https://cgi-lib.berkeley.edu/ex/fup.html")
driver.maximize_window()
time.sleep(3)

driver.find_element(By.NAME, "upfile").send_keys('E:\Selenium with Python\Section-1\L-3 original.pdf')
driver.find_element(By.NAME, "note").send_keys("Test Notes")
driver.find_element(By.XPATH, "//input[@type='submit']").click()

time.sleep(3)
driver.quit()
