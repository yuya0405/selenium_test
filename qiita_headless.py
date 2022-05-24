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

# Googleで右側にも検索結果が出たらエラー？？？
# 参考：https://qiita.com/y_sayama/items/ed0558c891db36fea83c

# stats = driver.find_element(by=By.ID, value="resultStats").text
# print(stats)

# for i, g in enumerate(driver.find_elements(By.CLASS_NAME, "g")):
#     print("------ " + str(i+1) + " ------")
#     r = g.find_element(By.CLASS_NAME, "r")
#     print(r.find_element(By.TAG_NAME, "h3").text)
#     print("\t" + r.find_element(By.TAG_NAME, "a").get_attribute("href"))
#     s = g.find_element(By.CLASS_NAME, "s")
#     print("\t" + s.find_element(By.CLASS_NAME, "st").text)

driver.save_screenshot('search_results.png')
driver.quit()
