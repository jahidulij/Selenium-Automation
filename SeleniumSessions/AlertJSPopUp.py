import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)

base_url = driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
time.sleep(3)

# Click for JS Alert
driver.find_element(By.XPATH, "//button[contains(text(),'Click for JS Alert')]").click()
time.sleep(3)
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
result = driver.find_element(By.XPATH, "//h4[contains(text(),'Result:')]")
result_msg = driver.find_element(By.ID, "result")
print(result.text + " " + result_msg.text)

# Click for JS Confirm
driver.find_element(By.XPATH, "//button[contains(text(),'Click for JS Confirm')]").click()
time.sleep(3)
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
# alert.dismiss()
result = driver.find_element(By.XPATH, "//h4[contains(text(),'Result:')]")
result_msg = driver.find_element(By.ID, "result")
print(result.text + " " + result_msg.text)

# Click for JS Prompt
driver.find_element(By.XPATH, "//button[contains(text(),'Click for JS Prompt')]").click()
time.sleep(3)
alert = driver.switch_to.alert
print(alert.text)
alert.send_keys("Test123")
# alert.accept()
alert.dismiss()
result = driver.find_element(By.XPATH, "//h4[contains(text(),'Result:')]")
result_msg = driver.find_element(By.ID, "result")
print(result.text + " " + result_msg.text)

driver.switch_to.default_content()

time.sleep(3)
driver.quit()
