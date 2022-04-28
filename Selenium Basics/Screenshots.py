import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(5)

driver.get("https://www.amazon.ca/")
driver.maximize_window()
print(driver.title)
time.sleep(3)

# Visible part Screenshot
# driver.get_screenshot_as_file('amazon.png')

# Full page Screenshot *** Must run in headless mode
S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
driver.set_window_size(S('Width'), S('Height'))
driver.find_element(By.TAG_NAME, 'body').screenshot('amazon_full_page_ss.png')

time.sleep(3)
driver.quit()
