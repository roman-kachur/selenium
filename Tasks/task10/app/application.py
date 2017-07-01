from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from Tasks.task10.pages.campaign_page import CampaignPage
from Tasks.task10.pages.checkout_page import CheckoutPage
import time


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        #self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(1)
        self.base_url = "http://localhost/litecart"
        self.campaign_tab = CampaignPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)

    def quit(self):
        time.sleep(2)
        self.driver.quit()

    def open_campaign(self):
        self.campaign_tab.open(self.base_url)

    def buy_first_product(self):
        # Condition: items in cart should increase:
        self.init_cart = self.get_items_from_cart()
        self.final_cart = self.init_cart + 1

        # Add it:
        self.campaign_tab.add_item_to_cart()
        self.campaign_tab.close_item()

        # Wait until cart's items is updated:
        self.campaign_tab.wait_for_cart(str(self.final_cart))

    def get_items_from_cart(self):
        # Check current items in the cart:
        return self.campaign_tab.check_items()

    def purge_cart(self):
        self.checkout_page.open()
        self.checkout_page.remove_items()