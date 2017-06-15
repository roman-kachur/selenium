from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

menu = a_driver.find_elements_by_xpath('//*[@id="app-"]')

for index in range(1, len(menu)):
	x_path = '//*[@id="box-apps-menu"]/li['+str(index)+']'
	print(x_path)
	a_driver.find_element_by_xpath(x_path).click()
	time.sleep(3)