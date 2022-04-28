import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)

base_url = driver.get("https://www.spicejet.com/")
driver.maximize_window()
time.sleep(3)
add_ons_element = driver.find_element(By.XPATH, "//div[contains(text(),'Add-ons')]")
action_chain = ActionChains(driver)
action_chain.move_to_element(add_ons_element).perform()

seat_meal_element = driver.find_element(By.XPATH, "//div[contains(text(),'Seat + Meal Combo')]").click()

time.sleep(10)
driver.quit()
