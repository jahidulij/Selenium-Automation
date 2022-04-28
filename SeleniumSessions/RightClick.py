import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)

base_url = driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
time.sleep(3)

# Double/ Context click
right_click_element = driver.find_element(By.XPATH, "//span[contains(text(),'right click me')]")
action_chain = ActionChains(driver)
action_chain.context_click(right_click_element).perform()

right_click_options = driver.find_elements(By.CSS_SELECTOR, "li.context-menu-item  span")
for option in right_click_options:
    print(option.text)
    if option.text == 'Copy':
        option.click()
        break


time.sleep(5)
driver.quit()
