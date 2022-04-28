from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
import time

browserName = "other"

if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == "ie":
    driver = webdriver.Ie(IEDriverManager().install())
else:
    print("Please pass the correct browser name: " + browserName)
    raise Exception("Driver is not found")

driver.implicitly_wait(3)
base_url = driver.get("https://app.hubspot.com/login")
driver.maximize_window()
driver.find_element(By.ID, "username").send_keys("naveenanimation30@gmail.com")
driver.find_element(By.ID, "password").send_keys("Test@12345")
driver.find_element(By.ID, "loginBtn").click()

print(driver.title)

time.sleep(4)
driver.quit()
