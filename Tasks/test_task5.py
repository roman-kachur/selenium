from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time


def test_product():
    an_url = 'http://localhost/litecart'

    #  Check it in Chrome:
    a_driver = webdriver.Chrome(ChromeDriverManager().install())
    a_driver.implicitly_wait(3)
    check_it(a_driver, an_url)

    # Check it in Firefox:
    #a_driver = webdriver.Firefox(GeckoDriverManager().install())
    a_driver = webdriver.Firefox()
    a_driver.implicitly_wait(3)
    check_it(a_driver, an_url)

    # Check it in IE:
    a_driver = webdriver.Ie(IEDriverManager().install())
    a_driver.implicitly_wait(3)
    check_it(a_driver, an_url)




def check_it(a_driver, an_url):
    # Open url
    a_driver.get(an_url)
    WebDriverWait(a_driver, 3).until(ec.title_is("My Store | Online Store"))

    # Select Campaign Product tab:
    camp_prod_tab_css = 'a[href="#campaign-products"]'
    #WebDriverWait(a_driver, 3).until(ec.presence_of_element_located((By.CSS_SELECTOR, camp_prod_tab_css)))
    capmaign_product = a_driver.find_element_by_css_selector(camp_prod_tab_css)
    capmaign_product.click()
    time.sleep(2)

    # Select first product:
    products_css = 'div[id="box-campaign-products"]'
    first_product_css = products_css + ' div[class^="col-xs"]:nth-child(1)'
    #WebDriverWait(a_driver, 3).until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, first_product_css)))
    first_product = a_driver.find_element_by_css_selector(first_product_css)

    # Get first item's properties on Main page:
    # Name:
    first_product_name_css = first_product_css + ' div[class="name"]'
    #WebDriverWait(a_driver, 3).until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, first_product_name_css)))
    first_product_name = a_driver.find_element_by_css_selector(first_product_name_css)
    a_name = first_product_name.get_attribute('textContent')

    # Regular Price value and style:
    first_product_regprice_css = first_product_css + ' s[class ="regular-price"]'
    #WebDriverWait(a_driver, 3).until(ec.presence_of_element_located((By.CSS_SELECTOR, first_product_regprice_css)))
    first_product_regprice = a_driver.find_element_by_css_selector(first_product_regprice_css)
    a_regvalue = first_product_regprice.get_attribute('textContent')
    a_regcolor = first_product_regprice.value_of_css_property("color")
    a_regstyle = first_product_regprice.value_of_css_property("text-decoration-line")

    # Campaign Price value and style:
    first_product_campprice_css = first_product_css + ' strong[class ="campaign-price"]'
    #WebDriverWait(a_driver, 3).until(ec.presence_of_element_located((By.CSS_SELECTOR, first_product_campprice_css)))
    first_product_campprice = a_driver.find_element_by_css_selector(first_product_campprice_css)
    a_campvalue = first_product_campprice.get_attribute('textContent')
    a_campcolor = first_product_campprice.value_of_css_property("color")
    a_campstyle = first_product_campprice.value_of_css_property("font-weight")

    # Finally, click on the first product:
    first_product.click()
    clicked_product_css = 'div[id="box-product"]'
    WebDriverWait(a_driver, 3).until(ec.visibility_of_element_located((By.CSS_SELECTOR, clicked_product_css)))

    # Get clicked item's properties:
    # Name:
    clicked_item_name_css = clicked_product_css + ' h1[class="title"]'
    #WebDriverWait(a_driver, 3).until(ec.presence_of_element_located((By.CSS_SELECTOR, clicked_item_name_css)))
    clicked_item_name = a_driver.find_element_by_css_selector(clicked_item_name_css)
    clicked_name = clicked_item_name.get_attribute('textContent')

    # Clicked Regular Price value and style:
    clicked_product_regprice_css = clicked_product_css + ' del[class ="regular-price"]'
    #WebDriverWait(a_driver, 3).until(ec.presence_of_element_located((By.CSS_SELECTOR, clicked_product_regprice_css)))
    clicked_product_regprice = a_driver.find_element_by_css_selector(clicked_product_regprice_css)
    clicked_regvalue = clicked_product_regprice.get_attribute('textContent')
    clicked_regcolor = clicked_product_regprice.value_of_css_property("color")
    clicked_regstyle = clicked_product_regprice.value_of_css_property("text-decoration-line")

    # Clicked Campaign Price value and style:
    clicked_product_campprice_css = clicked_product_css + ' strong[class ="campaign-price"]'
    #WebDriverWait(a_driver, 3).until(ec.presence_of_element_located((By.CSS_SELECTOR, clicked_product_campprice_css)))
    clicked_product_campprice = a_driver.find_element_by_css_selector(clicked_product_campprice_css)
    clicked_campvalue = clicked_product_campprice.get_attribute('textContent')
    clicked_campcolor = clicked_product_campprice.value_of_css_property("color")
    clicked_campstyle = clicked_product_campprice.value_of_css_property("font-weight")

    # Compare values:
    assert (a_name == clicked_name), "Product Name doesn't match"
    assert (a_regvalue == clicked_regvalue), "Product Regular Price doesn't match"
    assert (a_campvalue == clicked_campvalue), "Product Campaign Price doesn't match"
    assert (a_regcolor == clicked_regcolor), "Product Regular Color doesn't match"
    assert (a_campcolor == clicked_campcolor), "Product Campaign Color doesn't match"
    assert (a_regstyle == clicked_regstyle), "Product Regular Price Style doesn't match"
    assert (a_campstyle == clicked_campstyle), "Product Campaign Price Style doesn't match"

    # Logout:
    time.sleep(2)
    a_driver.quit()