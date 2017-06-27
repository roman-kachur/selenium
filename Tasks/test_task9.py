from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
import time

def test_log_driver():

    # Driver initialization:
    a_driver = EventFiringWebDriver(webdriver.Chrome(), MyListener())
    a_driver.implicitly_wait(1)

    # Repeat test4 in separate func:
    menu_walk(a_driver)

    # Exit the driver:
    a_driver.quit()


class MyListener(AbstractEventListener):
    def before_find(self, by, value, a_driver):
        print(by, value)

    def after_find(self, by, value, a_driver):
        print(by, value)

    def on_exception(self, exception, a_driver):
        print(exception)
        a_driver.get_screenshot_as_file('screen'+str(round(time.time()*1000))+'.png')


def menu_walk(a_driver):

    # Definitions:
    username = 'admin'
    password = 'admin'
    driver_wait = 2                     # 2 second for explicit waits.
    page_header_css = 'h1'              # Expected condition for assertions.
    an_url = "http://localhost/litecart/admin/"

    # Lets go. Open url:
    a_driver.get(an_url)
    # Wait for a header:
    WebDriverWait(a_driver, driver_wait).until(ec.title_is("My Store"))
    # Enter username:
    username_css_locator = 'input[name=username]'
    a_driver.find_element_by_css_selector(username_css_locator).send_keys(username)
    # Enter password:
    password_css_locator = 'input[name=password]'
    a_driver.find_element_by_css_selector(password_css_locator).send_keys(password)
    # Login:
    login_css_selector = 'button[name=login]'
    a_driver.find_element_by_css_selector(login_css_selector).click()
    # Wait for a header:
    WebDriverWait(a_driver, driver_wait).until(ec.title_is("My Store"))


    ## Walk through menus:

    # Wait for main menu:
    menu_css = 'li[id="app-"]'
    try:
        menu_presence = WebDriverWait(a_driver, driver_wait).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, menu_css)))
    except:
        print("Main menu was not found")
        a_driver.quit()

    menu = a_driver.find_elements_by_css_selector(menu_css)
    for index in range(1, len(menu) + 1):
        menu_item_css = menu_css + ':nth-child(' + str(index) + ')'
        WebDriverWait(a_driver, driver_wait).until(ec.element_to_be_clickable((By.CSS_SELECTOR, menu_item_css)))
        a_driver.find_element_by_css_selector(menu_item_css).click()
        assert (WebDriverWait(a_driver, driver_wait).until
                (ec.visibility_of_element_located((By.CSS_SELECTOR, page_header_css)))), "Element h1 not found"

        # Check for submenu:
        sub_menu_css = 'li[id^="doc-"]'
        try:
            sub_menu_presence = WebDriverWait(a_driver, driver_wait).until(
                ec.presence_of_all_elements_located((By.CSS_SELECTOR, sub_menu_css)))
        except:
            print("Submenu is absent here.")
        if sub_menu_presence:
            sub_menu = a_driver.find_elements_by_css_selector(sub_menu_css)
            for jndex in range(1, len(sub_menu) + 1):
                sub_menu_item_css = sub_menu_css + ':nth-child(' + str(jndex) + ')'
                WebDriverWait(a_driver, driver_wait).until(ec.element_to_be_clickable((By.CSS_SELECTOR, sub_menu_item_css)))

                ## Intentionally set wrong assertion for the test to fail:
                #if sub_menu_item_css == 'li[id^="doc-"]:nth-child(2)':
                #    page_header_css = 'h5'

                a_driver.find_element_by_css_selector(sub_menu_item_css).click()
                assert (WebDriverWait(a_driver, driver_wait).until
                        (ec.visibility_of_element_located((By.CSS_SELECTOR, page_header_css)))), "Element h1 not found"

    # Logout:
    logout_css_locator = 'i[class="fa fa-sign-out fa-lg"]'
    a_driver.find_element_by_css_selector(logout_css_locator).click()
    time.sleep(1)