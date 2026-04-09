import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import os
import math

link = "https://stepik.org/lesson/236895/step/1"

def load_config():
    parent_dir = os.path.dirname(os.path.dirname(__file__))
    config_path = os.path.join(parent_dir, 'config.json')

    if os.path.exists(config_path):
        with open(config_path) as config:
            return json.load(config)
    else:
        raise FileNotFoundError("Please create config.json from config.example.json")
    
config = load_config()
LOGIN = config['login']
PASSWORD = config['password']

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestCollectMessages():
    result_message = ""
    links_for_search = ["https://stepik.org/lesson/236895/step/1", 
                        "https://stepik.org/lesson/236896/step/1", 
                        "https://stepik.org/lesson/236897/step/1", 
                        "https://stepik.org/lesson/236898/step/1", 
                        "https://stepik.org/lesson/236899/step/1", 
                        "https://stepik.org/lesson/236903/step/1", 
                        "https://stepik.org/lesson/236904/step/1", 
                        "https://stepik.org/lesson/236905/step/1"]

    @pytest.mark.parametrize('links', links_for_search)
    def test_collect_messages(self, browser, links):
        browser.get(links)

        login_link = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='auth=login']"))
        ).get_attribute('href')
        
        browser.get(login_link)
        
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='login']"))
        ).send_keys(LOGIN)

        browser.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(PASSWORD)
        browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        time.sleep(3)

        answer = str(math.log(int(time.time())))

        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea"))
        ).send_keys(answer)

        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
        ).click()

        hint_text = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
        ).text

        if hint_text != "Correct!":
            self.result_message += hint_text + "\n"
        
        print(f"Сообщение для {links}: {hint_text}")

        assert hint_text == "Correct!"

        time.sleep(5)