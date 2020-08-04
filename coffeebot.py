# selenium project 1
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


driver.get("https://twitter.com/login")
print(driver.title)

user = driver.find_element_by_name("session[username_or_email]")
secret = driver.find_element_by_name("session[password]")

user.send_keys("user")
driver.implicitly_wait(1)
secret.send_keys("pass")
driver.implicitly_wait(1)
secret.send_keys(Keys.RETURN)

driver.get("https://twitter.com/compose/tweet")

tweet = driver.find_element_by_xpath("//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div")
tweet.send_keys("coffee time")
tweet.send_keys(Keys.CONTROL, Keys.RETURN)

time.sleep(5)

driver.quit()