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

    # No Implicit wait. We rely on Explicit waits:
    #a_driver.implicitly_wait(1)

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
    wait = WebDriverWait(a_driver, 3)
    wait_for_submenu = WebDriverWait(a_driver, 0.5)
    username = 'admin'
    password = 'admin'
    page_header_css = 'h1'              # Expected condition for assertions.
    an_url = "http://localhost/litecart/admin/"

    # Lets go. Open url:
    a_driver.get(an_url)
    # Wait for a header:
    wait.until(ec.title_is("My Store"))

    # Enter username:
    username_css_locator = 'input[name=username]'
    wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, username_css_locator)))
    a_driver.find_element_by_css_selector(username_css_locator).send_keys(username)
    # Enter password:
    password_css_locator = 'input[name=password]'
    wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, password_css_locator)))
    a_driver.find_element_by_css_selector(password_css_locator).send_keys(password)
    # Login:
    login_css_selector = 'button[name=login]'
    wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, login_css_selector)))
    a_driver.find_element_by_css_selector(login_css_selector).click()


    # Walk through menu:

    # Wait for main menu:
    menu_css = 'li[id="app-"]'
    menu_presence = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, menu_css)))
    menu = a_driver.find_elements_by_css_selector(menu_css)

    for index in range(1, len(menu) + 1):
        menu_item_css = menu_css + ':nth-child(' + str(index) + ')'
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, menu_item_css)))
        #print(menu_item_css)
        a_driver.find_element_by_css_selector(menu_item_css).click()
        assert (wait.until
                (ec.visibility_of_element_located((By.CSS_SELECTOR, page_header_css)))), "Element h1 not found"

        # Check for submenu:
        sub_menu_css = 'li[id^="doc-"]'
        try:
            sub_menu_presence = wait_for_submenu.until(
                ec.presence_of_all_elements_located((By.CSS_SELECTOR, sub_menu_css)))
        except :
            sub_menu_presence = False
        if sub_menu_presence:
            sub_menu = a_driver.find_elements_by_css_selector(sub_menu_css)
            for jndex in range(1, len(sub_menu) + 1):
                sub_menu_item_css = sub_menu_css + ':nth-child(' + str(jndex) + ')'
                wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, sub_menu_item_css)))
                #print(sub_menu_item_css)
                a_driver.find_element_by_css_selector(sub_menu_item_css).click()
                assert (wait.until
                        (ec.visibility_of_element_located((By.CSS_SELECTOR, page_header_css)))), "Element h1 not found"

    # Logout:
    logout_css_locator = 'i[class="fa fa-sign-out fa-lg"]'
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, logout_css_locator)))
    a_driver.find_element_by_css_selector(logout_css_locator).click()