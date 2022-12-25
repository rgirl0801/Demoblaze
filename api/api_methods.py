import requests
from http import HTTPStatus

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


def view_product(id_product):
    response = requests.post(f'{api_url}view', json={"id": id_product})
    assert response.status_code == HTTPStatus.OK
    return response


def view_cart(data):
    response = requests.post(f'{api_url}viewcart', json=data)
    assert response.status_code == HTTPStatus.OK
    return response


def add_to_cart(data):
    response = requests.post(f'{api_url}addtocart', json=data)
    assert response.status_code == HTTPStatus.OK
    return response


def delete_item_from_cart(item_id):
    response = requests.post(f'{api_url}deleteitem', json={"id": item_id})
    assert response.status_code == HTTPStatus.OK
    return response


def delete_cart():
    response = requests.post(f'{api_url}deletecart', json={"cookie": POSITIVE_API_CREDS['username']})
    assert response.status_code == HTTPStatus.OK
    return response.json()
