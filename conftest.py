import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name', action='store', default="chrome",
        help="Choose browser: chrome or firefox")

    parser.addoption(
        "--language", actiom="store", default="en",
        help="chose any language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        user_language = request.config.getoption("language")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language}, )
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        user_language = request.config.getoption("language")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        fp.set_preference('excludeSwitches', ['enable-logging'])
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()