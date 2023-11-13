from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

default_password = "secret_sauce"

def test_user_add_all_items():
    # Given dasboard "standard_user"
    browser = Chrome()
    browser.get("https://www.saucedemo.com")
    assert browser.find_element(By.CLASS_NAME, "login_logo").is_displayed
    browser.find_element(By.ID, "username").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys(default_password)
    browser.find_element(By.ID, "login-button").click()
    products = browser.find_elements(By.CLASS_NAME, "inventory_item")
    for i in products:
        print(i)
test_user_add_all_items()
    # When user type "standard_user" and "secret_sauce" credential

    # When user tap all items to cart
    
    # And user go to cart page
    # Then user displayed all items that added