from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

def test_product(an_url = 'http://localhost/litecart'):

    # Initialize a driver:
    options = webdriver.ChromeOptions()
    options.add_argument("start-fullscreen")
    a_driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

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
    first_prod_xpath = '//*[@id="box-campaign-products"]/div/div/div/a[1]'
    WebDriverWait(a_driver, 3).until(ec.presence_of_element_located((By.XPATH, first_prod_xpath)))
    first_product = a_driver.find_element_by_xpath(first_prod_xpath)
    first_product.click()
    time.sleep(3)

    # Logout:
    a_driver.quit()