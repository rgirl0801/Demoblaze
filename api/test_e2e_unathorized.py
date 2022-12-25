import pytest

from api.api_methods import *

ID_SAMSUNG_S6 = '391b2964-f0ae-cea4-b7c3-29c736de9ee1'
ID_NOKIA = 'aba3c63c-1888-fdea-db57-6324f08b233e'
token = "user=0d25c327-a320-ef3c-f6bb-2843e379ad0c"

# @pytest.fixture()
# def token():
#     return get_token()


def test_delete_item_from_cart():
    add_to_cart_by_id(token=token, id_uniq=ID_SAMSUNG_S6)
    number_of_products = len(view_cart(cookie=token, authorized_flag=False))
    assert number_of_products != 0
    delete_item_from_cart(id_uniq=ID_SAMSUNG_S6)
    number_of_product_after_delete = len(view_cart(cookie=token, authorized_flag=False))
    assert number_of_products - number_of_product_after_delete == 1, 'Deletion did not occur'


def test_view_cart_with_auth():
    add_to_cart_by_id(token=token, id_uniq=ID_NOKIA)
    assert len(view_cart(cookie=token, authorized_flag=False)) != 0, 'Cart is empty after adding'


def test_delete_entire_cart_with_auth():
    add_to_cart_by_id(token=token, id_uniq=ID_NOKIA)
    delete_cart()
    assert len(view_cart(cookie=token, authorized_flag=False)) == 0, 'Cart is not empty'
