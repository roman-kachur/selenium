import pytest
from Tasks.task10.app.application import Application
from .data_provider import items_to_add


app = Application()
#@pytest.mark.parametrize("items_to_add", items_to_add)
def test_can_add_item_to_cart(app):

    app.open()  # Navigate to Campaign Products tab.

    for i in range(items_to_add):

        items_before = app.get_items_from_cart()
        app.buy_first_product()
        items_after = app.get_items_from_cart()

        assert items_after - items_before == 1