from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time


def switch_to_new_window(a_driver, old_windows):
    new_window = [i for i in a_driver.window_handles if i not in old_windows]
    return new_window[0]


def test_external_links():

    username = 'admin'
    password = 'admin'
    an_url = "http://localhost/litecart/admin/"

    # Initialize a driver:
    #a_driver = webdriver.Ie(IEDriverManager().install())
    #a_driver = webdriver.Chrome(ChromeDriverManager().install())
    a_driver = webdriver.Firefox()
    a_driver.implicitly_wait(3)
    wait= WebDriverWait(a_driver, 6)

    a_driver.get(an_url)
    # Wait for a header:
    wait.until(ec.title_is("My Store"))

    # Enter username:
    username_css_locator = 'input[name=username]'
    a_driver.find_element_by_css_selector(username_css_locator).send_keys(username)

    # Enter password:
    password_css_locator = 'input[name=password]'
    a_driver.find_element_by_css_selector(password_css_locator).send_keys(password)

    # Login:
    login_css_selector = 'button[name=login]'
    a_driver.find_element_by_css_selector(login_css_selector).click()

    # Wait for a menu:
    main_manu_css = 'ul[id="box-apps-menu"]'
    wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, main_manu_css)))

    # ===============================
    # Enter Countries menu:
    countries_menu_css = 'li[id="app-"]:nth-child(3)'
    countries_menu = a_driver.find_element_by_css_selector(countries_menu_css)
    countries_menu.click()

    # Remember main window:
    first_window = a_driver.current_window_handle

    # Add new country:
    add_new_country_css = 'a[class="btn btn-default"]'
    add_new_country = a_driver.find_element_by_css_selector(add_new_country_css)
    add_new_country.click()

    # Get all external links:
    external_links_css = 'i[class="fa fa-external-link"]'
    external_links = a_driver.find_elements_by_css_selector(external_links_css)

    # Go through the external lists:
    for a_link in external_links:
        old_windows = a_driver.window_handles
        a_link.click()

        # Check new window was opened:
        new_window = switch_to_new_window(a_driver, old_windows)
        assert new_window, print("No new windows were opened")
        if new_window:
            a_driver.switch_to.window(new_window)
            a_driver.close()
            a_driver.switch_to.window(first_window)


    # Logout:
    logout_css_locator = 'i[class="fa fa-sign-out fa-lg"]'
    a_driver.find_element_by_css_selector(logout_css_locator).click()

    # Close the driver:
    time.sleep(1)
    a_driver.quit()