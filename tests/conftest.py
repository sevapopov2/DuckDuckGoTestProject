import json
import pytest
import selenium.webdriver


@pytest.fixture
def config(scope='session'):
    # Read json file with parameters
    with open('config.json') as config_file:
        config = json.load(config_file)
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0
    return config


@pytest.fixture
def browser(config):
    if config['browser'] == 'Firefox':
        web_browser = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        web_browser = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        web_browser = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')
    web_browser.implicitly_wait(config['implicit_wait'])
    yield web_browser
    web_browser.quit()
