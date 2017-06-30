from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class CampaignTab:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)

    def open(self, base_url):
        self.driver.get(base_url)

        # Select Campaign Product tab:
        self.camp_prod_tab_css = 'a[href="#campaign-products"]'
        self.capmaign_product = self.driver.find_element_by_css_selector(self.camp_prod_tab_css)
        self.capmaign_product.click()
        return self

    def add_item_to_cart(self):
        # Select and click on the first product on the tab:
        self.products_css = 'div[id="box-campaign-products"]'
        self.first_product_css = self.products_css + ' div[class^="col-xs"]:nth-child(1)'
        self.first_product = self.driver.find_element_by_css_selector(self.first_product_css)
        self.first_product.click()

        # If present, try to choose item's Size=Small:
        self.size_css = 'select[class ="form-control"] option[value="Small"]'
        try:
            self.size_presence = WebDriverWait(self.driver, 1).until(
                ec.presence_of_element_located((By.CSS_SELECTOR, self.size_css)))
        except:
            self.size_presence = False

        if self.size_presence:
            self.driver.find_element_by_css_selector(self.size_css).click()

        # Click Button 'Add to cart':
        self.add_button_css = 'button[name="add_cart_product"]'
        self.add_button = self.driver.find_element_by_css_selector(self.add_button_css)
        self.add_button.click()
        return self

    def close_item(self):
        # Close item's window:
        self.close_button_css = 'button[aria-label="Close"]'
        self.close_button = self.driver.find_element_by_css_selector(self.close_button_css)
        self.close_button.click()

    def check_items(self):
        self.cart_items_css = 'span[class="quantity"]'
        self.cart_items = self.driver.find_element_by_css_selector(self.cart_items_css)
        return int(self.cart_items.text)

    def wait_for_cart(self, final_cart):
        # Wait until cart's items updated:
        self.wait.until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, self.cart_items_css), final_cart))
        return self