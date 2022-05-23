import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs
from webdriver_manager.chrome import ChromeDriverManager

chrome_service = fs.Service(ChromeDriverManager().install())

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options, service=chrome_service)  # 今は chrome_options= ではなく options=

driver.get('https://www.google.com/')
print(driver.title)

search_box = driver.find_element(by=By.NAME, value="q")
search_box.send_keys('ChromeDriver')
search_box.submit()
print(driver.title)

driver.save_screenshot('search_results.png')
driver.quit()
