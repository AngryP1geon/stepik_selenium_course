import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.execute_script("document.title='Script executing';alert('Robots at work');")

# Время, чтобы скопировать результат
time.sleep(10)

# Закрываем браузер
browser.quit()