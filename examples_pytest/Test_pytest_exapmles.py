import pytest


def test_screenshot_on_test_failure(browser):
    # driver = webdriver.Firefox()
    browser.get("https://google.com")
    assert True

def test_screenshot_on_test_pass(browser):
    
    assert True
@pytest.mark.skip
def test_screenshot_on_test_skip(browser):
    
    assert True