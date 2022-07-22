from pages.search import DuckDuckGoSearchPage
from pages.result import DuckDuckGoResultPage
import pytest


@pytest.mark.parametrize('phrase', ['panda', 'python', 'cat'])
def test_basic_duckduckgo_search(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    # Load the page
    search_page.load()
    # Search for panda
    search_page.search(phrase)
    assert phrase == result_page.search_input_value()
    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0
    assert phrase in result_page.title()