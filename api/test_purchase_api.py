from http import HTTPStatus

import requests

from links import api_url


def test_view_all_items():
    for id in range(1, 15):
        response = requests.post(f'{api_url}view', json={"id": id})
        print(response.json())
        assert response.status_code == HTTPStatus.OK


def test_purchase_api():
    requests.post(f'{api_url}view', json={"id": 1})
    data = {
        "id": "26c5430e-fc3a-8bfd-c34c-3ecd5c3d8388",
        "cookie": "user=0d25c327-a320-ef3c-f6bb-2843e379ad0c",
        "prod_id": 1,
        "flag": False
    }
    response1 = requests.post(f'{api_url}addtocart', json=data)
    print(response1)
    data1 = {
        "cookie": "user=0d25c327-a320-ef3c-f6bb-2843e379ad0c",
        "flag": False
    }
    response2 = requests.post(f'{api_url}viewcart', json=data)
    print(response2.json())
