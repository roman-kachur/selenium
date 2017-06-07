from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_google():
    #a_driver = webdriver.Chrome()
    a_driver = webdriver.Chrome(ChromeDriverManager().install())
    an_url = "https://google.com/"
    a_driver.get(an_url)
    a_driver.find_element_by_name('q').send_keys('webdriver')
    a_driver.find_element_by_name('btnG').click()
    WebDriverWait(a_driver, 3).until(ec.title_is("webdriver - Пошук Google"))
    time.sleep(3)
    a_driver.quit()

#test_google()