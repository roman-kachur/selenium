from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time


def test_product(an_url = 'http://localhost/litecart'):

    # Select and Initialize a driver:
    a_driver = webdriver.Chrome(ChromeDriverManager().install())
    #a_driver = webdriver.Ie(IEDriverManager().install())

    # Open url
    a_driver.get(an_url)
    WebDriverWait(a_driver, 3).until(ec.title_is("My Store | Online Store"))
    time.sleep(1)

    # Select Campaign Product tab:
    camp_prod_tab_xpath = '//*[@id="content"]/ul/li[1]'
    WebDriverWait(a_driver, 3).until(ec.presence_of_element_located((By.XPATH, camp_prod_tab_xpath)))
    capmaign_product = a_driver.find_element_by_xpath(camp_prod_tab_xpath)
    time.sleep(3)

    # Select first product:
    first_product_xpath = '//*[@id="box-campaign-products"]/div/div/div/a[1]'
    WebDriverWait(a_driver, 3).until(ec.presence_of_element_located((By.XPATH, first_product_xpath)))
    first_product = a_driver.find_element_by_xpath(first_product_xpath)

    # Get first item's properties on Main page:
    # Name:
    first_product_name_xpath = '//*[@id="box-campaign-products"]/div/div/div/a[1]/div[2]/div[1]'
    first_product_name = a_driver.find_element_by_xpath(first_product_name_xpath)
    a_name = first_product_name.get_attribute('textContent')

    # Regular Price value and style:
    first_product_regprice_xpath = '//*[@id="box-campaign-products"]/div/div/div/a[1]/div[2]/div[3]/s'
    first_product_regprice = a_driver.find_element_by_xpath(first_product_regprice_xpath)
    a_regvalue = first_product_regprice.get_attribute('textContent')
    a_regcolor = first_product_regprice.value_of_css_property("color")
    a_regstyle = first_product_regprice.value_of_css_property("text-decoration-line")

    # Campaign Price value and style:
    first_product_campprice_xpath = '//*[@id="box-campaign-products"]/div/div/div/a[1]/div[2]/div[3]/strong'
    first_product_campprice = a_driver.find_element_by_xpath(first_product_campprice_xpath)
    a_campvalue = first_product_campprice.get_attribute('textContent')
    a_campcolor = first_product_campprice.value_of_css_property("color")
    a_campstyle = first_product_campprice.value_of_css_property("font-weight")


    # Click on selected item:
    first_product.click()
    clicked_product_xpath = '//*[@id="box-product"]'
    WebDriverWait(a_driver, 3).until(ec.presence_of_element_located((By.XPATH, clicked_product_xpath)))
    #time.sleep(3)

    # Get ckicked item's properties:
    # Name:
    clicked_item_name_xpath = '//*[@id="box-product"]/div[1]/div[2]/h1'
    clicked_item_name = a_driver.find_element_by_xpath(clicked_item_name_xpath)
    clicked_name = clicked_item_name.get_attribute('textContent')

    # Clicked Regular Price value and style:
    clicked_product_regprice_xpath = '//*[@id="box-product"]/div[1]/div[3]/div/div[1]/del'
    clicked_product_regprice = a_driver.find_element_by_xpath(clicked_product_regprice_xpath)
    clicked_regvalue = clicked_product_regprice.get_attribute('textContent')
    clicked_regcolor = clicked_product_regprice.value_of_css_property("color")
    clicked_regstyle = clicked_product_regprice.value_of_css_property("text-decoration-line")

    # Clicked Campaign Price value and style:
    clicked_product_campprice_xpath = '//*[@id="box-product"]/div[1]/div[3]/div/div[1]/strong'
    clicked_product_campprice = a_driver.find_element_by_xpath(clicked_product_campprice_xpath)
    clicked_campvalue = clicked_product_campprice.get_attribute('textContent')
    clicked_campcolor = clicked_product_campprice.value_of_css_property("color")
    clicked_campstyle = clicked_product_campprice.value_of_css_property("font-weight")


    # Print out values before comparision:
    print("First Items's attributes are: ", a_name, a_regvalue, a_regcolor, a_regstyle,
          a_campvalue, a_campcolor, a_campstyle)

    print("Clicked Item's attributes are: ", clicked_name, clicked_regvalue, clicked_regcolor, clicked_regstyle,
          clicked_campvalue, clicked_campcolor, clicked_campstyle)

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