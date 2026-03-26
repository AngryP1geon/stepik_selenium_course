import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

browser.find_element(By.CSS_SELECTOR, "[name='firstname']").send_keys('Дмитрий')
browser.find_element(By.CSS_SELECTOR, "[name='lastname']").send_keys('Шаравин')
browser.find_element(By.CSS_SELECTOR, "[name='email']").send_keys('mail@example.com')
browser.find_element(By.ID, "file").send_keys(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'step_8_1.txt'))
browser.find_element(By.TAG_NAME, "button").click()

# Время, чтобы скопировать результат
time.sleep(10)

# Закрываем браузер
browser.quit()