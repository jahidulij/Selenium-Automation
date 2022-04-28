import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)

base_url = driver.get("http://londonfreelance.org/courses/frames/index.html")
driver.maximize_window()
time.sleep(3)

# driver.switch_to.frame(2)
# driver.switch_to.frame('main')
frame_element = driver.find_element(By.NAME, 'main')
driver.switch_to.frame(frame_element)

headerValue = driver.find_element(By.CSS_SELECTOR, "body > h2").text
print(headerValue)

driver.switch_to.default_content()
driver.switch_to.parent_frame()

time.sleep(3)
driver.quit()
