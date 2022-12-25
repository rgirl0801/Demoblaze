import requests

from constants import POSITIVE_API_CREDS
from links import api_url


def get_token():
    response = requests.post(f'{api_url}login', json=POSITIVE_API_CREDS)
    token = response.json().split(' ')[1]
    return token


def view_product(id_product):
    response = requests.post(f'{api_url}view', json={"id": id_product})
    return response


def view_cart(data):
    response = requests.post(f'{api_url}viewcart', json=data)
    return response


def add_to_cart(data):
    response = requests.post(f'{api_url}addtocart', json=data)
    return response


def delete_item_from_cart(item_id):
    response = requests.post(f'{api_url}deleteitem', json={"id": item_id})
    return response


def delete_cart():
    response = requests.post(f'{api_url}deletecart', json={"cookie": POSITIVE_API_CREDS['username']})
    return response.json()
