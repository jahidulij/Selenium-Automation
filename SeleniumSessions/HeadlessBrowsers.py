import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

option = webdriver.ChromeOptions()
# option.headless = True
option.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
driver.implicitly_wait(5)

driver.get("https://www.amazon.ca/")
driver.maximize_window()
print(driver.title)
time.sleep(3)




time.sleep(3)
driver.quit()
