from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys

default_username = "standard_user"
default_password = "secret_sauce"

def test_using_valid_credential():
    # Given user open saucedemo.com in Chrome
    browser = Chrome()
    browser.get("https://www.saucedemo.com")
    assert browser.find_element(By.CLASS_NAME, "login_logo").is_displayed
    # When user type "standard_user" and "secret_sauce" credential
    browser.find_element(By.ID, "user-name").send_keys(default_username)
    browser.find_element(By.ID, "password").send_keys(default_password)
    # And user tap login button
    browser.find_element(By.ID, "login-button").click()
    # Then user directed to dashboard page
    assert str("https://www.saucedemo.com/inventory.html") == browser.current_url
    browser.quit()


def test_blank_username():
    # Given user open saucedemo.com in Chrome
    browser = Chrome()
    browser.get("https://www.saucedemo.com")
    assert browser.find_element(By.CLASS_NAME, "login_logo").is_displayed
    # When user type password "secret_sauce" only
    browser.find_element(By.ID, "user-name").clear()
    browser.find_element(By.ID, "password").send_keys(default_password)
    # And user tap login button
    browser.find_element(By.ID, "login-button").click()
    # Then user receive error notification about credential requirement
    assert str("https://www.saucedemo.com/inventory.html") != browser.current_url
    assert str("Epic sadface: Username is required") == browser.find_element(By.XPATH, '//h3[@data-test="error"]').text
    browser.quit()


def test_blank_password():
    # Given user open saucedemo.com in Chrome
    browser = Chrome()
    browser.get("https://www.saucedemo.com")
    assert browser.find_element(By.CLASS_NAME, "login_logo").is_displayed
    # When user type username "standard_user" only
    browser.find_element(By.ID, "user-name").send_keys(default_username)
    browser.find_element(By.ID, "password").clear()
    # And user tap login button
    browser.find_element(By.ID, "login-button").click()
    # Then user receive error notification about credential requirement
    assert str("https://www.saucedemo.com/inventory.html") != browser.current_url
    assert str("Epic sadface: Password is required") == browser.find_element(By.XPATH, '//h3[@data-test="error"]').text
    browser.quit()


def test_using_invalid_credential():
    # Given user open saucedemo.com in Chrome
    browser = Chrome()
    browser.get("https://www.saucedemo.com")
    assert browser.find_element(By.CLASS_NAME, "login_logo").is_displayed
    # When user type wrong username or password
    browser.find_element(By.ID, "user-name").send_keys(default_username)
    browser.find_element(By.ID, "password").send_keys(default_username)
    # And user tap login button
    browser.find_element(By.ID, "login-button").click()
    # Then user receive error notification about credential requirement
    assert str("https://www.saucedemo.com/inventory.html") != browser.current_url
    assert str("Epic sadface: Username and password do not match any user in this service") == browser.find_element(By.XPATH, '//h3[@data-test="error"]').text
    browser.quit()


def test_using_without_credential():
    # Given user open saucedemo.com in Chrome
    browser = Chrome()
    browser.get("https://www.saucedemo.com")
    assert browser.find_element(By.CLASS_NAME, "login_logo").is_displayed
    # When user does'nt input credential
    browser.find_element(By.ID, "user-name").clear()
    browser.find_element(By.ID, "password").clear()
    # And user tap login button
    browser.find_element(By.ID, "login-button").click()
    # Then user receive error notification about credential requirement
    assert str("https://www.saucedemo.com/inventory.html") != browser.current_url
    assert str("Epic sadface: Username is required") == browser.find_element(By.XPATH, '//h3[@data-test="error"]').text
    browser.quit()


def test_using_locked_credential():
    # Given user open saucedemo.com in Chrome
    browser = Chrome()
    browser.get("https://www.saucedemo.com")
    assert browser.find_element(By.CLASS_NAME, "login_logo").is_displayed
    # When user type "locked_out_user" and default password
    browser.find_element(By.ID, "user-name").send_keys("locked_out_user")
    browser.find_element(By.ID, "password").send_keys(default_password)
    # And user tap login button
    browser.find_element(By.ID, "login-button").click()
    # Then user receive error notification about credential requirement
    assert str("https://www.saucedemo.com/inventory.html") != browser.current_url
    assert str("Epic sadface: Sorry, this user has been locked out.") == browser.find_element(By.XPATH, '//h3[@data-test="error"]').text
    browser.quit()


def _login_another_username(username):
    # Given user open saucedemo.com in Chrome
    browser = Chrome()
    browser.get("https://www.saucedemo.com")
    assert browser.find_element(By.CLASS_NAME, "login_logo").is_displayed
    # When user type "locked_out_user" and default password
    browser.find_element(By.ID, "user-name").send_keys(username)
    browser.find_element(By.ID, "password").send_keys(default_password)
    # And user tap login button
    browser.find_element(By.ID, "login-button").click()
    # Then user directed to dashboard page
    assert str("https://www.saucedemo.com/inventory.html") == browser.current_url
    browser.quit()


def test_login_problem_user():
    _login_another_username("problem_user")


def test_login_performance_glitch_user():
    _login_another_username("performance_glitch_user")


def test_login_error_user():
    _login_another_username("error_user")


def test_login_visual_user():
    _login_another_username("visual_user")