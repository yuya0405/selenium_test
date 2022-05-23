import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.google.com/')
time.sleep(1)
search_box = driver.find_element(by=By.NAME, value="q")
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(1)
driver.quit()
