import pytest

from api.api_helpers import *


@pytest.fixture()
def token():
    return get_token()


def test_get_item_price(token):
    data = {
        "id": "1615386a-022c-3fb0-e347-df271eae8dc9",
        "cookie": token,
        "prod_id": 2,
        "flag": True
    }
    print(view_cart(data).json()['Items'][0])


def test_e2e(token):
    data = {
        "id": "1615386a-022c-3fb0-e347-df271eae8dc9",
        "cookie": token,
        "prod_id": 2,
        "flag": True
    }
    print(add_to_cart(data))
    print(view_cart(data).json())
    assert 'Item deleted' in delete_cart()


@pytest.mark.parametrize("given_id", ['1', '2', '3'])
def test_view(given_id):
    response = view_product(id_product=given_id)
    print(response)


def test_delete_item(token):
    prod_id = "81f5592d-0486-0247-a108-20385cd91db7"
    data = {
        "id": prod_id,
        "cookie": token,
        "prod_id": 1,
        "flag": True
    }
    print(add_to_cart(data))
    print(delete_item_from_cart(prod_id).json())
