import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)

base_url = driver.get("https://jqueryui.com/resources/demos/droppable/default.html")
driver.maximize_window()
time.sleep(3)

# Drag and drop

source_element = driver.find_element(By.ID, 'draggable')
target_element = driver.find_element(By.ID, 'droppable')

action_chain = ActionChains(driver)
# action_chain.drag_and_drop(source_element, target_element).perform()
action_chain.click_and_hold(source_element).move_to_element(target_element).release().perform()

time.sleep(10)
driver.quit()
