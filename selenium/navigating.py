from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

url = 'http://github.com'

driver.get(url)
driver.maximize_window()

search_input = driver.find_element_by_name('q')

time.sleep(2)

search_input.send_keys('python')

time.sleep(2)

# search_input.submit()
search_input.send_keys(Keys.ENTER)

time.sleep(2)

titles = driver.find_elements(by=By.CSS_SELECTOR,value='.repo-list-item .f4 a')

for element in titles:
    print(element.text)

time.sleep(10)

driver.close()