from api.api_methods import *


def test_qty_all_products():
    assert len(get_all_products()) == 15


def test_view_all_items():
    for prod_id in range(1, 15):
        print(view_product(prod_id))


def test_get_price():
    print(view_product(1)['price'])