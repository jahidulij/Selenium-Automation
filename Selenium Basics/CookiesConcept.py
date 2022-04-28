import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)

base_url = driver.get("https://www.reddit.com/")
driver.maximize_window()
time.sleep(3)

print(driver.get_cookies())
driver.add_cookie({
    'name': 'PythonCookies',
    'domain': 'reddit.com',
    'value': 'PythonJ'
})

cookies = driver.get_cookies()
for cook in cookies:
    print(cook)


time.sleep(3)
driver.quit()
