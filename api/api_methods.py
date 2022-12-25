from http import HTTPStatus

import requests

from constants import POSITIVE_API_CREDS
from links import api_url


def get_token():
    response = requests.post(f'{api_url}login', json=POSITIVE_API_CREDS)
    assert response.status_code == HTTPStatus.OK
    token = response.json().split(' ')[1]
    return token


def login(credentials):
    response = requests.post(f'{api_url}login', json=credentials)
    assert response.status_code == HTTPStatus.OK
    return response.json()


def check_auth(token):
    response = requests.post(f'{api_url}check', json={"token": token})
    assert response.status_code == HTTPStatus.OK


def get_all_products():
    response_1 = requests.get(f'{api_url}entries')
    items1 = response_1.json()['Items']
    response_2 = requests.post(f'{api_url}pagination', json={"id": "9"})
    items2 = response_2.json()['Items']
    return items1 + items2


def get_all_products_from_first_page():
    response = requests.get(f'{api_url}entries')
    items = response.json()['Items']
    assert response.status_code == HTTPStatus.OK
    assert len(items) == 9
    return response.json()


def get_all_products_from_second_page():
    response = requests.post(f'{api_url}pagination', json={"id": "9"})
    items = response.json()['Items']
    assert response.status_code == HTTPStatus.OK
    assert len(items) == 6
    return response.json()


def view_product(id_product: int):
    """Json with items"""
    response = requests.post(f'{api_url}view', json={"id": id_product})
    assert response.status_code == HTTPStatus.OK
    return response.json()


def view_cart(cookie: str, authorized_flag: bool):
    """Json with items"""
    data = {
        "cookie": cookie,
        "flag": authorized_flag
    }
    response = requests.post(f'{api_url}viewcart', json=data)
    assert response.status_code == HTTPStatus.OK
    return response.json()['Items']


def add_to_cart_by_id(token: str, id_uniq: str):
    data = {
        "id": id_uniq,
        "cookie": token,
        "prod_id": 2,
        "flag": True
    }
    response = requests.post(f'{api_url}addtocart', json=data)
    assert response.status_code == HTTPStatus.OK
    return response


def delete_item_from_cart(id_uniq):
    response = requests.post(f'{api_url}deleteitem', json={"id": id_uniq})
    assert response.status_code == HTTPStatus.OK
    return response


def delete_cart():
    response = requests.post(f'{api_url}deletecart', json={"cookie": POSITIVE_API_CREDS['username']})
    assert response.status_code == HTTPStatus.OK
    return response.json()
