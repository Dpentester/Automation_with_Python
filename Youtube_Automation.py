# import webdriver
from selenium import webdriver

# import time
import time

# open the browser
driver = webdriver.Chrome()

# maximize the window
driver.maximize_window()


# ive the link to access
driver.get("https://www.youtube.com")

# Identify the youtube search box and provide xpath
searchbox = driver.find_element_by_name('search_query')
searchbox.send_keys("Python")
time.sleep(5)

# Provide the xpath of searchbutton inorder to search
searchbutton = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button')
searchbutton.click()
time.sleep(5)

# Close the browser
driver.close()