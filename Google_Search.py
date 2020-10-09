# import webdriver form selenium
from selenium import webdriver

# set the chrome path and set destination to driver
driver = webdriver.Chrome()
driver.get("https://www.google.com")

# searchbox
searchbox = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
searchbox.send_keys('https://www.alphahalf.com')

#searchbutton
searchbutton = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
searchbutton.click()
