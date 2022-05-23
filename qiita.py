import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())
chrome_service = fs.Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service)

driver.get('https://www.google.com/')
time.sleep(1)
search_box = driver.find_element(by=By.NAME, value="q")
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(1)
driver.quit()
