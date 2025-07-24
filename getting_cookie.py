from selenium import webdriver
import time
import pickle

url = "https://www.linkedin.com/jobs/"

driver = webdriver.Chrome()
driver.get(url)

time.sleep(200)

with open("cookies.pkl", "wb") as a:
    pickle.dump(driver.get_cookies(),a)

driver.quit()