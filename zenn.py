from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#特殊なキーの入力
from selenium.webdriver.common.keys import Keys
#セレクトボックスの操作
from selenium.webdriver.support.ui import Select
#ホバーを操作
from selenium.webdriver.common.action_chains import ActionChains
#明示的な待機
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#接続
driver = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://www.google.co.jp/'
driver.get(url)

#終了
driver.quit()
