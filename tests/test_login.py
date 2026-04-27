import pytest
from utils.driver_setup import get_driver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.mark.parametrize("username,password,expected_url", [
    ("tomsmith", "SuperSecretPassword!", "secure"),
    ("tomsmith", "wrongpass", "secure"),
])
def test_login(driver, username, password, expected_url):
    login_page = LoginPage(driver)
    login_page.open("https://the-internet.herokuapp.com/login")

    login_page.login(username, password)

    try:
        assert expected_url in driver.current_url
    except:
        driver.save_screenshot("fail.png")
        raise