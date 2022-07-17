import pytest
import selenium.webdriver

@pytest.fixture
def browser():
    web_browser = selenium.webdriver.Chrome()
    web_browser.implicitly_wait(10)
    yield web_browser
    web_browser.quit()