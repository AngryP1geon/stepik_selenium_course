from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = browser.find_element(By.ID, "book")

WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
button.click()

x = browser.find_element(By.ID, 'input_value').text
result = calc(x)

input = browser.find_element(By.ID, 'answer')
browser.execute_script("return arguments[0].scrollIntoView(true);", input)
input.send_keys(result)
browser.find_element(By.ID, "solve").click()

# Время, чтобы скопировать результат
time.sleep(10)

# Закрываем браузер
browser.quit()