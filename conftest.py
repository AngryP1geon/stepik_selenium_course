import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='ru',
                     help="Choose user language")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': language})
    firefox_options = FirefoxOptions()
    firefox_options.set_preference('intl.accept_languages', language)

    browser_name = request.config.getoption("browser_name")
    browser = None

    if browser_name == "chrome":
        print("\nStart chrome browser for test...")
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        print("\nStart firefox browser for test...")
        browser = webdriver.Firefox(options=firefox_options)
    else:
        raise pytest.UsageError("--browser-name should be chrome or firefox")

    yield browser

    print("\nQuit browser...")
    browser.quit()