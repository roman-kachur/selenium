from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import IEDriverManager
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_google(an_url = "https://google.com/"):
    #a_driver = webdriver.Chrome()
    #options = webdriver.ChromeOptions()
    #options.add_argument("start-fullscreen")
    #a_driver = webdriver.Chrome(ChromeDriverManager().install(),
    #                           desired_capabilities={"chromeOptions": {"args": ["--start-fullscreen"]}})
    #a_driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options = options)
    a_driver = webdriver.Chrome(ChromeDriverManager().install())
    #a_driver = webdriver.Ie(IEDriverManager().install())

    a_driver.get(an_url)
    a_driver.find_element_by_name('q').send_keys('webdriver')
    a_driver.find_element_by_name('btnG').click()
    WebDriverWait(a_driver, 3).until(ec.title_is("webdriver - Пошук Google"))

    cookies = a_driver.get_cookies()
    print(cookies)
    a_driver.delete_all_cookies()

    time.sleep(3)
    a_driver.quit()

#test_google()
