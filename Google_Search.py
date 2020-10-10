# import webdriver
from selenium import webdriver
import time
# open the browser
driver = webdriver.Chrome()

# provide the url to browse 
driver.get("https://www.google.com")

# searchbox
searchbox = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
searchbox.send_keys('alphahalf')


# searchbutton
searchbutton = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
searchbutton.click()

time.sleep(3)

# close the browser
driver.close()