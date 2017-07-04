import pytest
from Tasks.task10.app.application import Application
import time


#@pytest.mark.parametrize("items", items_to_add)
def test_can_add_remove_items_from_cart(app):

    # Navigate to Campaign Products tab:
    app.open_campaign()

    # Add first item three times:
    for i in range(3):

        items_before = app.get_items_from_cart()

        app.buy_first_product()

        items_after = app.get_items_from_cart()

        assert items_after - items_before == 1

    # Purge the cart:
    app.purge_cart()

    assert app.is_cart_empty(), print("There are still some items in the cart!")
