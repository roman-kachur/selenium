from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)

    def open(self):
        # Navigate to Checkout page:
        self.cart_css = 'div[class="content"] div[class="title"]'
        self.cart = self.driver.find_element_by_css_selector(self.cart_css)
        self.cart.click()
        return self

    def remove_items(self):
        # Check that selected items are still present in the cart:
        self.items_css = 'table[class="items table table-striped data-table"] tbody'
        self.items = self.driver.find_element_by_css_selector(self.items_css)

        # find all buttons 'Remove button':
        self.remove_buttons_css = 'button[class="btn btn-danger"]'
        self.remove_buttons = self.driver.find_elements_by_css_selector(self.remove_buttons_css)
        # remove_buttons[0].click()

        while self.remove_buttons:
            self.remove_buttons[0].click()
            self.wait.until(ec.staleness_of(self.items))
            self.wait.until(ec.staleness_of(self.remove_buttons[0]))
            self.remove_buttons = self.driver.find_elements_by_css_selector(self.remove_buttons_css)

    def check_shopping_cart(self):
        # Returns if Shopping Cart holds any items:
        self.items_css = 'tr[class="item"]'
        self.items = self.driver.find_elements_by_css_selector(self.items_css)
        return bool(self.items)
