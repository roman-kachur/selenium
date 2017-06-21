from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

def test_add_new_item():

    username = 'admin'
    password = 'admin'
    an_url = "http://localhost/litecart/admin/"

    # Initialize a driver:
    #a_driver = webdriver.Ie(IEDriverManager().install())
    a_driver = webdriver.Chrome(ChromeDriverManager().install())
    #a_driver = webdriver.Firefox()
    a_driver.implicitly_wait(5)


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

    # Enter Catalogue menu:
    catalogue_main_menu_css = 'li[id="app-"]:nth-child(2)'
    catalogue_main_menu = a_driver.find_element_by_css_selector(catalogue_main_menu_css)
    catalogue_main_menu.click()
    catalogue_submenu_css = 'ul[id="box-apps-menu"] li[id="doc-catalog"]'
    catalogue_submenu = a_driver.find_element_by_css_selector(catalogue_submenu_css)
    catalogue_submenu.click()

    # Enter 'Add New Product' page:
    new_prod_btn_text = 'Add New Product'
    new_prod_btn = a_driver.find_element_by_link_text(new_prod_btn_text)
    new_prod_btn.click()

    # Add new item:
    #image:
    local_image_path = 'c:/Users/maint/Desktop/Log/Jira.png'
    image_field_css = 'input[name="new_images[]"]'
    image_field = a_driver.find_element_by_css_selector(image_field_css)
    image_field.send_keys(local_image_path)

    #name:
    a_name = 'Yet another item'
    name_field_css = 'input[name="name[en]"]'
    name_field = a_driver.find_element_by_css_selector(name_field_css)
    name_field.send_keys(a_name)



    # Save the item:
    button_save_css = 'button[name="save"]'
    button_save = a_driver.find_element_by_css_selector(button_save_css)
    button_save.click()





    # Logout:
    time.sleep(3)
    logout_css_locator = 'i[class="fa fa-sign-out fa-lg"]'
    a_driver.find_element_by_css_selector(logout_css_locator).click()

    time.sleep(3)
    a_driver.quit()

