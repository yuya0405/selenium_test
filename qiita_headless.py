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

for g_h3 in driver.find_elements(by=By.CSS_SELECTOR, value=".g h3"):
    print(g_h3.text)

# stats = driver.find_element(by=By.ID, value="resultStats").text
# print(stats)

driver.save_screenshot('search_results.png')
driver.quit()
