import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

x = browser.find_element(By.ID, 'input_value').text
result = calc(x)

input = browser.find_element(By.ID, 'answer')
browser.execute_script("return arguments[0].scrollIntoView(true);", input)
input.send_keys(result)

browser.find_element(By.ID, 'robotCheckbox').click()
browser.find_element(By.ID, 'robotsRule').click()
browser.find_element(By.TAG_NAME, 'button').click()

# Время, чтобы скопировать результат
time.sleep(10)

# Закрываем браузер
browser.quit()