import pytest
from Tasks.task10.app.application import Application
from .data_provider import items_to_add
import time


def test_can_add_remove_items_from_cart(app):

    # Navigate to Campaign Products tab:
    app.open_campaign()

    # Add first item three times:
    for i in range(items_to_add):
        items_before = app.get_items_from_cart()
        #print("Before: ", items_before)
        app.buy_first_product()
        items_after = app.get_items_from_cart()
        #print("After: ", items_after)
        assert items_after - items_before == 1

    # Purge the cart:
    app.purge_cart()
