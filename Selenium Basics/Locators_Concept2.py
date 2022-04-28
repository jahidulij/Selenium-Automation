from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
base_url = driver.get("https://www.amazon.ca/")
driver.maximize_window()
print(driver.title)

linksList = driver.find_elements(By.TAG_NAME, 'a')
print(len(linksList))

for link in linksList:
    print(link.text)
    print(link.get_attribute('href'))

images = driver.find_elements(By.TAG_NAME, "img")
print(len(images))

for image in images:
    print(image.get_attribute('src'))


time.sleep(4)
driver.quit()
