from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\\Python Driver\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://www.google.com/")
print("Page Title: " + driver.title)

driver.find_element(By.NAME, "q").send_keys("Selenium")

optionList = driver.find_elements(By.CSS_SELECTOR, "ul.G43f7e li")
print(len(optionList))

for option in optionList:
    print(option.text)
    if option.text == 'selenium webdriver':
        option.click()
        break


time.sleep(3)
driver.quit()
