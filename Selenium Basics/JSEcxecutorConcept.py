import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.amazon.ca/")

# best_sellers = driver.find_element(By.LINK_TEXT, 'Best Sellers')
# driver.execute_script("arguments[0].click();", best_sellers)
# title = driver.execute_script("return document.title")
# print(title)
# driver.execute_script("history.go(0);")
# # driver.execute_script("alert('Hello, Selenium!');")
# inner_text = driver.execute_script("return document.documentElement.innerText;")
# print(inner_text)
# driver.execute_script("arguments[0].style.border = '3px solid red';", best_sellers)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # Scroll at BOTTOM
# driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);") # Scroll at TOP
driver.implicitly_wait(5)
# back_to_top = driver.find_element(By.LINK_TEXT, "Back to top")
# driver.execute_script("arguments[0].scrollIntoView(true);", back_to_top)
# back_to_top.click()
# print(driver.execute_script("return navigator.userAgent;")) # Browser info
# driver.execute_script("document.getElementById('username').value='test@mail.com';")



time.sleep(3)
driver.close()


