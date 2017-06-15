from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time


def test_sidemenu():

    # Initialize a driver:
    options = webdriver.ChromeOptions()
    options.add_argument("start-fullscreen")
    a_driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

    # Open url
    an_url = "http://localhost/litecart/admin/"
    username = 'admin'
    password = 'admin'
    a_driver.get(an_url)
    WebDriverWait(a_driver, 3).until(ec.title_is("My Store"))
    time.sleep(3)

    # Enter username:
    WebDriverWait(a_driver, 3).until(
        ec.presence_of_element_located((By.XPATH, '//*[@id="box-login"]/form/div[1]/div[1]/div/input')))
    a_driver.find_element_by_xpath('//*[@id="box-login"]/form/div[1]/div[1]/div/input').send_keys(username)
    time.sleep(1)

    # Enter password:
    WebDriverWait(a_driver, 3).until(
        ec.presence_of_element_located((By.XPATH, '//*[@id="box-login"]/form/div[1]/div[2]/div/input')))
    a_driver.find_element_by_xpath('//*[@id="box-login"]/form/div[1]/div[2]/div/input').send_keys(password)
    time.sleep(1)

    # Login:
    WebDriverWait(a_driver, 3).until(
        ec.presence_of_element_located((By.XPATH, '//*[@id="box-login"]/form/div[2]/button')))
    a_driver.find_element_by_xpath('//*[@id="box-login"]/form/div[2]/button').click()
    WebDriverWait(a_driver, 3).until(ec.title_is("My Store"))
    time.sleep(3)

    # Walk through menu:
    menu = a_driver.find_elements_by_xpath('//*[@id="app-"]')
    for index in range(1, len(menu) + 1):
        x_path = '//*[@id="box-apps-menu"]/li[' + str(index) + ']'
        print(x_path)
        a_driver.find_element_by_xpath(x_path).click()
        time.sleep(2)
        # Check for submenu:
        sub_menu = a_driver.find_elements_by_xpath(x_path + '/ul/li')
        if sub_menu:
            for jndex in range(1, len(sub_menu) + 1):
                sub_x_path = x_path + '/ul/li[' + str(jndex) + ']'
                print(sub_x_path)
                a_driver.find_element_by_xpath(sub_x_path).click()
                time.sleep(2)

    # Logout:
    WebDriverWait(a_driver, 3).until(ec.presence_of_element_located((By.XPATH, '// *[ @ id = "shortcuts"] / a[5] / i')))
    a_driver.find_element_by_xpath('// *[ @ id = "shortcuts"] / a[5] / i').click()
    time.sleep(3)
    a_driver.quit()


