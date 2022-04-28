import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.freshworks.com/")

wait = WebDriverWait(driver, 10)
footer_links = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, '.footer-nav li')))
print(len(footer_links))
for element in footer_links:
    print(element.text)


time.sleep(3)
driver.close()


