from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

username = "mdsamanngp@gmail.com"
password = "Saman@4025"

driver.get("https://www.linkedin.com/login")

# Enter username
username_input = driver.find_element(By.ID, "username")
username_input.send_keys(username)

# Enter password
password_input = driver.find_element(By.ID, "password")
password_input.send_keys(password)

# Click login button
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Wait for login to complete
time.sleep(5)

# Example: write extract to a file
with open('extract.txt', 'w') as f:
    f.write('Logged in to LinkedIn successfully')
driver.quit()