from http import HTTPStatus

import requests

from links import api_url


def test_entries():
    response = requests.get(f'{api_url}entries')
    items = response.json()['Items']
    assert response.status_code == HTTPStatus.OK
    assert len(items) == 9


def test_pagination():
    response = requests.post(f'{api_url}pagination', json={"id": "9"})
    items = response.json()['Items']
    assert response.status_code == HTTPStatus.OK
    assert len(items) == 6


def test_view_all_items():
    for id in range(1, 15):
        response = requests.post(f'{api_url}view', json={"id": id})
        print(response.json())
        assert response.status_code == HTTPStatus.OK
