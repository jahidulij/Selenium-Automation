import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)

base_url = driver.get("https://classic.crmpro.com/index.html")
driver.maximize_window()
time.sleep(3)

username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
login = driver.find_element(By.XPATH, "//input[@type='submit']")

action_chain = ActionChains(driver)
action_chain.send_keys_to_element(username, "batchautomation")
action_chain.send_keys_to_element(password, "Test@12345")
action_chain.click(login).perform()

time.sleep(5)
driver.quit()
