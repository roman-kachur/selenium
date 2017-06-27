from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

def test_cart():

    # Definitions:
    an_url = 'http://localhost/litecart/'

    # Initialize a driver:
    #a_driver = webdriver.Ie(IEDriverManager().install())
    #a_driver = webdriver.Firefox()
    a_driver = webdriver.Chrome(ChromeDriverManager().install())
    a_driver.implicitly_wait(2)
    wait = WebDriverWait(a_driver, 4)

    a_driver.get(an_url)
    # Wait for a header:
    wait.until(ec.title_is("My Store | Online Store"))

    #time.sleep(25)     # Here, I manually add few other items to the cart.

    # Select Campaign Product tab:
    camp_prod_tab_css = 'a[href="#campaign-products"]'
    capmaign_product = a_driver.find_element_by_css_selector(camp_prod_tab_css)
    capmaign_product.click()

    # Select and click on the first product on the tab:
    products_css = 'div[id="box-campaign-products"]'
    first_product_css = products_css + ' div[class^="col-xs"]:nth-child(1)'
    first_product = a_driver.find_element_by_css_selector(first_product_css)
    first_product.click()

    # Switch to full page view:
    full_page_view_css = 'div[id="view-full-page"]'
    full_page_view = a_driver.find_element_by_css_selector(full_page_view_css)
    full_page_view.click()

    # Choose item's Size=Small:
    size_css = 'select[class ="form-control"] option[value="Small"]'
    size = a_driver.find_element_by_css_selector(size_css)
    size.click()

    # Check current items in the cart:
    cart_items_css = 'span[class="quantity"]'
    cart_items = a_driver.find_element_by_css_selector(cart_items_css)

    # Button 'Add to cart':
    add_button_css = 'button[name="add_cart_product"]'
    add_button = a_driver.find_element_by_css_selector(add_button_css)

    # Add it to the cart three times:
    for i in range(3):
        # Check current items in the cart:
        items = cart_items.text

        # Click Add button:
        add_button.click()

        # Wait until cart's items is updated:
        plus_one = str(int(items) + 1)
        wait.until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, cart_items_css), plus_one))

        ## Close item's window:
        #close_button_css = 'button[aria-label="Close"]'
        #close_button = a_driver.find_element_by_css_selector(close_button_css)
        #close_button.click()


    # Navigate to the cart:
    cart_css = 'div[class="content"] div[class="title"]'
    cart = a_driver.find_element_by_css_selector(cart_css)
    cart.click()

    # Check that selected items are still present in the cart:
    items_css = 'table[class="items table table-striped data-table"] tbody'
    items = a_driver.find_element_by_css_selector(items_css)

    # find all buttons 'Remove button':
    remove_buttons_css = 'button[class="btn btn-danger"]'
    remove_buttons = a_driver.find_elements_by_css_selector(remove_buttons_css)
    #remove_buttons[0].click()

    while remove_buttons:
        remove_buttons[0].click()
        wait.until(ec.staleness_of(items))
        wait.until(ec.staleness_of(remove_buttons[0]))
        remove_buttons = a_driver.find_elements_by_css_selector(remove_buttons_css)

    # Close the driver:
    time.sleep(1)
    a_driver.quit()