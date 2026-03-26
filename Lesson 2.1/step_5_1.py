from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Получаем значение x
    x = browser.find_element(By.ID, "input_value").text

    # Рассчитываем функцию от x
    fx = calc(x)

    # Записываем полученный результат f(x) в поле для ввода
    browser.find_element(By.ID, "answer").send_keys(fx)

    # Отмечаем чек-бокс
    browser.find_element(By.ID, "robotCheckbox").click()

    # Выбираем радио-кнопку
    browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()

    # Отправляем результат
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

finally:
    # Время, чтобы скопировать результат
    time.sleep(10)

    # Закрываем браузер
    browser.quit()