from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Python Driver\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://www.worldometers.info/")
print("Page Title: " + driver.title)
driver.implicitly_wait(3)
driver.find_element(By.LINK_TEXT, "Population").click()
driver.implicitly_wait(6)
bd = driver.find_element(By.LINK_TEXT, "Bangladesh")
# bd = driver.find_element((By.XPATH, "//a[contains(text(),'Bangladesh')]"))
driver.execute_script("arguments[0].scrollIntoView(true);", bd)
bd.click()

driver.implicitly_wait(5)
name = driver.find_element(By.XPATH, "//*[@id='maincounter-wrap']/h1")
print(name.text)
population = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[2]/ul/li[1]/strong[2]")
print(population.text)
# print(name.text + ": " + population.text)

time.sleep(3)
driver.quit()
