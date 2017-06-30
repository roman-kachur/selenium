from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Tasks.task10.pages.campaign_tab import CampaignTab


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.base_url = "http://localhost/litecart"
        self.campaign_tab = CampaignTab(self.driver)

    def quit(self):
        self.driver.quit()

    def open(self):
        self.campaign_tab.open(self.base_url)

    def buy_first_product(self):
        self.campaign_tab.add_item_to_cart()
        self.campaign_tab.close_item()

    def get_items_from_cart(self):
        # Check current items in the cart:
        self.cart_items_css = 'span[class="quantity"]'
        self.cart_items = self.driver.find_element_by_css_selector(self.cart_items_css)
        return int(self.cart_items)
