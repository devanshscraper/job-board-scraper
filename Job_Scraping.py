from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
import time
import random
import pickle

def random_time(num1=5, num2=30):
    return (random.randrange(num1, num2) / 10)

url = "https://www.linkedin.com/feed/"

#driver = webdriver.Chrome().maximize_window()
while True:
    jobs = input("Enter Job Name: ")
    try:
        a = int(jobs)
    except:
        break
    else:
        print("Please enter a valid name")
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 60)
driver.get(url)
time.sleep(random_time())
with open("cookies.pkl", "rb") as a:
    cookies = pickle.load(a)

for cookie in cookies:
    driver.add_cookie(cookie)
driver.get(url)
print(driver.title)
#//a[contains(@data-view-name, "jobs")]
#element = driver.find_element(By.XPATH, "//a[contains(@href, '/jobs/')]")
job_button = wait.until(ec.presence_of_element_located((By.XPATH, "//a[contains(@href, '/jobs/')]")))
#print(job_button.get_attribute("outerHTML"))
job_button.click()

print("Clicked")
time.sleep(2)
search = wait.until(ec.presence_of_element_located((By.XPATH, "//input[@aria-label='Search by title, skill, or company']")))

search.send_keys("Game Development")
search.send_keys(Keys.RETURN)

time.sleep(random_time(20, 60))
# Loop Here start tomorrow
# # This must be in the loop as the pages are changing
str_1 = ""


while True:
    body = wait.until(ec.presence_of_element_located((By.TAG_NAME, "body")))
    time.sleep(random_time(10, 20))
    jobs_on_page = wait.until(ec.presence_of_element_located((By.XPATH, "//a[contains(@href, '/jobs/view') and contains(@class, 'job-card')]")))
    jobs_on_page.click()
    time.sleep(random_time(15, 30))
    body.send_keys(Keys.END)
    time.sleep(random_time(15, 30))
    jobs_on_page = wait.until(ec.presence_of_all_elements_located((By.XPATH, "//a[contains(@href, '/jobs/view') and contains(@class, 'job-card')]")))
    Company = driver.find_elements(By.XPATH, "//div[contains(@id , 'ember')]/span[@dir = 'ltr']")
    print(len(jobs_on_page))



    for i, job in enumerate(jobs_on_page):
        print("Test pass 1")
        job.click()

        data = wait.until(ec.presence_of_all_elements_located((By.CLASS_NAME, "mt4")))
        str_1 += (f"Total companies: {len(Company)}\n")
        str_1 += (f"Total Jobs: {len(jobs_on_page)}\n")
        title = job.text.strip().split('\n')[0]
        str_1 += "Title: " + title + "\n"
        str_1 += f"Company: {Company[i].text.strip()}\n"

        print("Total companies:", len(Company))
        print("Total Jobs: ", len(jobs_on_page))
        print("Title: ", job.text.strip().split("\n")[0])
        print("Company: " + Company[i].text.strip())
        try:
            remote = driver.find_element(By.XPATH, "//span[@dir = 'ltr' and contains(@class, 'job-details-jobs')]")
            str_1 += "Remote: " + remote.text.strip() + "\n"
            print("Remote: " + remote.text.strip())
        except:
            str_1 += "Remote Not Found"
            print("Remote: Not Found")
        try:
            skills = driver.find_element(By.XPATH, "//button[@dir = 'ltr' and contains(@class, 'job-details-jobs')]")
            str_1 += skills.text.strip() + "\n"
            print(skills.text.strip())
        except:
            str_1 += "Skills: Not Found" + "\n"
            print("Skills: Not Found")
        for dta in data:
            if (len(dta.text.split()) > 200):
                print("Test 2 pass")
                print(dta.text.strip())
                str_1 += dta.text.strip() + "\n"
        print("\n\n\n\n\n\n\n\n\n\n")
        ActionChains(driver).scroll_to_element(job).perform()
        time.sleep(random_time(20, 45))

    next = driver.find_element(By.XPATH, "//button[@aria-label = 'View next page']")
    time.sleep(random_time(10,15))
    next.click()

    time.sleep(random_time(30, 40))
    with open("Jobs.txt" , "a", encoding="utf-8") as x:
        x.write(str_1)
    str_1 = ""
driver.quit()
