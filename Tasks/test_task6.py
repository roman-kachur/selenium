from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import time

def test_add_new_item():

    username = 'admin'
    password = 'admin'
    an_url = "http://localhost/litecart/admin/"

    # Initialize a driver:
    #a_driver = webdriver.Ie(IEDriverManager().install())
    a_driver = webdriver.Chrome(ChromeDriverManager().install())
    #a_driver = webdriver.Firefox()
    a_driver.implicitly_wait(3)
    wait = WebDriverWait(a_driver, 6)
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
    # image:
    local_image_path = os.path.abspath('0009.jpg')
    image_field_css = 'input[name="new_images[]"]'
    image_field = a_driver.find_element_by_css_selector(image_field_css)
    image_field.send_keys(local_image_path)

    # name:
    a_name = 'Mona Lisa'
    name_field_css = 'input[name="name[en]"]'
    name_field = a_driver.find_element_by_css_selector(name_field_css)
    name_field.send_keys(a_name)

    # code:
    a_code = '0009'
    code_field_css = 'input[name="code"]'
    code_field = a_driver.find_element_by_css_selector(code_field_css)
    code_field.send_keys(a_code)

    # Click "Enable" button:
    enable_button_css = 'label[class="btn btn-default"]'
    enable_button = a_driver.find_element_by_css_selector(enable_button_css)
    enable_button.click()

    # Quantity:
    quantity = 4
    quantity_field_css = 'input[class="form-control"][name="quantity"]'
    quantity_field = a_driver.find_element_by_css_selector(quantity_field_css)
    quantity_field.send_keys(quantity)

    # Weight:
    weight = '1.2'
    weight_field_css = 'input[class="form-control"][name="weight"]'
    weight_field = a_driver.find_element_by_css_selector(weight_field_css)
    weight_field.clear()
    weight_field.send_keys(weight)

    # Product Groups:
    gender_checkbox_css = 'div[class=form-group]'
    unisex_css = gender_checkbox_css + ' input[value="1-3"]'
    unisex = a_driver.find_element_by_css_selector(unisex_css)
    unisex.click()

    # ======================================
    # Go to Information tab:
    information_tab_css = 'ul[class="nav nav-tabs"] a[href="#tab-information"]'
    information_tab = a_driver.find_element_by_css_selector(information_tab_css)
    information_tab.click()

    # Manufacturer option:
    manufacturer_option_css = 'select[name="manufacturer_id"] option[value="1"]'
    manufacturer_option = a_driver.find_element_by_css_selector(manufacturer_option_css)
    manufacturer_option.click()

    # Keywords:
    keywords = "Leo da Vinci"
    keywords_field_css = 'input[name="keywords"]'
    keywords_field = a_driver.find_element_by_css_selector(keywords_field_css)
    keywords_field.send_keys(keywords)

    # Description:
    description = "Not for resale"
    description_field_css = 'div[class="row"] div[class="trumbowyg-editor"]'
    description_field = a_driver.find_element_by_css_selector(description_field_css)
    description_field.send_keys(description)

    # ================================
    # Go to Prices tab:
    prices_tab_css = 'ul[class="nav nav-tabs"] a[href="#tab-prices"]'
    prices_tab = a_driver.find_element_by_css_selector(prices_tab_css)
    prices_tab.click()

    # Select currency:
    currency_drop_down_css = 'select[name = "purchase_price_currency_code"]'
    euro_currency_css = currency_drop_down_css + ' option[value = "USD"]'
    euro_currency = a_driver.find_element_by_css_selector(euro_currency_css)
    euro_currency.click()

    # Set the price:
    price = '4096'
    usd_price_css = 'input[class="form-control"][name="prices[USD]"]'
    usd_price = a_driver.find_element_by_css_selector(usd_price_css)
    usd_price.clear()
    usd_price.send_keys(price)

    # Add campaign price:
    add_campaigns_css = 'table[id="table-campaigns"] a[class="add"][title="Add"]'
    add_campaigns = a_driver.find_element_by_css_selector(add_campaigns_css)
    add_campaigns.click()

    campaign = '10'
    campaign_field_css = 'input[name="campaigns[new_1][percentage]"]'
    campaign_field = a_driver.find_element_by_css_selector(campaign_field_css)
    campaign_field.clear()
    campaign_field.send_keys(campaign)

    # ===========================================
    # Save the item:
    button_save_css = 'button[name="save"]'
    button_save = a_driver.find_element_by_css_selector(button_save_css)
    button_save.click()


    # Logout:
    logout_css_locator = 'i[class="fa fa-sign-out fa-lg"]'
    a_driver.find_element_by_css_selector(logout_css_locator).click()

    time.sleep(3)
    a_driver.quit()