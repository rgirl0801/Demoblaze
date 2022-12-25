from http import HTTPStatus

import pytest
import requests
from api.api_helpers import get_token

from links import api_url

@pytest.fixture()
def token():
    return get_token()


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


@pytest.mark.parametrize("given_id", [1, 2, 3])
def test_purchase_api3(given_id, token):
    requests.post(f'{api_url}view', json={"id": given_id})
    data = {
          "id": "5ebdb548-836b-5a3a-c695-43e8b3e76e28",
          "cookie": "S2F0ZUZveDExNjcyNTI1",
          "prod_id": 2,
          "flag": True
        }
    response1 = requests.post(f'{api_url}addtocart', json=data)
    print(response1.json())
    # data1 = {
    #     "cookie": "user=0d25c327-a320-ef3c-f6bb-2843e379ad0c",
    #     "flag": False
    # }
    # response2 = requests.post(f'{api_url}viewcart', json=data)
    # print(response2.json())

