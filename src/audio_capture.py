from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# variabilize video 
# various platform support needed

URL = "https://www.youtube.com"


driver = webdriver.Chrome()

driver.get(URL) 
assert "YouTube" in driver.title
elem = driver.find_element(By.NAME, "q") 
elem.clear()
elem.send_keys(Keys.RETURN)
assert "Not found" not in driver.page_source
driver.close()
