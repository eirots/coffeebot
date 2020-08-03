# selenium tutorial 1
from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://twitter.com")
print(driver.title)
driver.quit()