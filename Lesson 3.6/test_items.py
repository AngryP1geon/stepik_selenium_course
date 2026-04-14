from selenium.webdriver.common.by import By
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_presence(browser):
    browser.get(link)
    add_to_basket_buttons = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(add_to_basket_buttons) > 0, 'Кнопка добавления в корзину не найдена'