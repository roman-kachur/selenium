from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time


def test_sidemenu():

    username = 'admin'
    password = 'admin'
    an_url = "http://localhost/litecart/admin/"

    # Initialize a driver:
    #a_driver = webdriver.Ie(IEDriverManager().install())
    a_driver = webdriver.Chrome(ChromeDriverManager().install())
    #a_driver = webdriver.Firefox()
    a_driver.implicitly_wait(3)

    a_driver.get(an_url)
    # Wait for a header:
    WebDriverWait(a_driver, 3).until(ec.title_is("My Store"))

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
    WebDriverWait(a_driver, 3).until(ec.title_is("My Store"))
    time.sleep(3)

    # Walk through menu:
    menu = a_driver.find_elements_by_xpath('//*[@id="app-"]')

    for index in range(1, len(menu) + 1):
        menu_item_x_path = '//*[@id="box-apps-menu"]/li[' + str(index) + ']'
        print(menu_item_x_path)
        a_driver.find_element_by_xpath(menu_item_x_path).click()
        assert (WebDriverWait(a_driver, 3).until
                (ec.visibility_of_element_located((By.XPATH, '//*[@id="main"]/h1')))), "Element h1 not found"

        # Check for submenu:
        sub_menu = a_driver.find_elements_by_xpath(menu_item_x_path + '/ul/li')
        if sub_menu:
            for jndex in range(1, len(sub_menu) + 1):
                sub_menu_item_x_path = menu_item_x_path + '/ul/li[' + str(jndex) + ']'
                print(sub_menu_item_x_path)
                a_driver.find_element_by_xpath(sub_menu_item_x_path).click()
                assert (WebDriverWait(a_driver, 3).until
                        (ec.visibility_of_element_located((By.XPATH, '//*[@id="main"]/h1')))), "Element h1 not found"

    # Logout:
    logout_css_locator = 'i[class="fa fa-sign-out fa-lg"]'
    a_driver.find_element_by_css_selector(logout_css_locator).click()

    time.sleep(3)
    a_driver.quit()