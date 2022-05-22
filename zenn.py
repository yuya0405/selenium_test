from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#接続
driver = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://www.google.co.jp/'
driver.get(url)

#終了
driver.quit()
