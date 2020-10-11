# import webdriver
from selenium import webdriver

# import email and password from credentials
from Credentials import email, password

# import time
import time

# Initialize the dirver to open the browser
driver = webdriver.Chrome()

# Maximize the window
driver.maximize_window()

# Provide URL to navigate
driver.get('https://www.facebook.com')
time.sleep(3)

# Xpath of email
loginMail = driver.find_element_by_xpath('//*[@id="email"]')

# provide email address
loginMail.send_keys(email)

# Xpath of password
loginPassword = driver.find_element_by_xpath('//*[@id="pass"]')

# provide password
loginPassword.send_keys(password)
time.sleep(3)

# path of Login
nextButton = driver.find_element_by_xpath('//*[@id="u_0_b"]')

# Click login
nextButton.click()
time.sleep(10)

# Close the browser
driver.close()
