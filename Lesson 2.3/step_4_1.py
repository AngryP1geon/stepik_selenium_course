import os
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

browser.find_element(By.TAG_NAME, "button").click()
browser.switch_to.alert.accept()
time.sleep(2)
browser.find_element(By.ID, "answer").send_keys(calc(browser.find_element(By.ID, "input_value").text))
browser.find_element(By.TAG_NAME, "button").click()

# Время, чтобы скопировать результат
time.sleep(10)

# Закрываем браузер
browser.quit()