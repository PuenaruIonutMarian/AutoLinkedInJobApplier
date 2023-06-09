from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time

URL = "THE LINK AFTER YOU SEARCH THE WISHED POSITION ON LINKEDIN"
passw = "LI ACCOUNT PASSD"
usern = "LI EMAIL ADDRESS"
PHONE = "YOUR Phone Number"

ser = Service(r"THE ADDRESS IN YOUR COMPUTER                 \chromedriver_win32\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
driver.get(URL)

sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()
time.sleep(5)
email_addr = driver.find_element(By.NAME, "session_key")
email_addr.send_keys(usern)
passw_key = driver.find_element(By.NAME, "session_password")
passw_key.send_keys(passw)
button = driver.find_element(By.CSS_SELECTOR, "form button")
button.click()

#Locate the apply button
# time.sleep(5)
# save_button = driver.find_element(By.XPATH, "//*[@id='main']/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button")
# save_button.click()

#If application requires phone number and the field is empty, then fill in the number.
# time.sleep(5)
# phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
# if phone.text == "":
#     phone.send_keys(PHONE)

#Submit the application
# submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
# submit_button.click()

time.sleep(5)


job_offers = driver.find_elements(By.CSS_SELECTOR, ".scaffold-layout__list-container li")


for job_offer in job_offers:
    ActionChains(driver).scroll_to_element(job_offer).perform()
    time.sleep(1)
    try:
        job_container = job_offer.find_element(By.CLASS_NAME, "job-card-container")
    except NoSuchElementException:
        continue
    else:
        job_container.click()

        time.sleep(2)

        save_job_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
        save_job_button.click()
        save_job_button.send_keys(Keys.END)

        time.sleep(2)

        follow_company_button = driver.find_element(By.CLASS_NAME, "follow")
        follow_company_button.click()