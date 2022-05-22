from selenium import webdriver
import chromedriver_binary # 自動でPATHが通る

#接続
driver = webdriver.Chrome()

url = 'https://www.google.co.jp/'
driver.get(url)

#終了
driver.quit()
