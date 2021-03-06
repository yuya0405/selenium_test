import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

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

# 完全マッチ
for a in driver.find_elements(by=By.LINK_TEXT, value="このページを訳す"):
    print(a.get_attribute("href"))

# 部分マッチ
for a in driver.find_elements(by=By.PARTIAL_LINK_TEXT, value="訳す"):
    print(a.get_attribute("href"))

# ホバーするものがない？？？

# # ホバー（マウスオーバーする）
# actions = ActionChains(driver)
# actions.move_to_element(
#     driver.find_element(by=By.CLASS_NAME, value="name")
# ).perform()  # hoverする

# ドラッグ＆ドロップするものがない？？？

# src = driver.find_element_by_name("source")
# tgt = driver.find_element_by_name("target")
# actions.drag_and_drop(src, tgt).perform()

driver.save_screenshot('search_results.png')
driver.quit()
