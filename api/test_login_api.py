from http import HTTPStatus

import pytest
import requests

from Links import api_url
from api.api_helpers import get_token
from constants import POSITIVE_API_CREDS, NEGATIVE_API_CREDS


@pytest.fixture()
def token():
    return get_token()


@pytest.mark.usefixtures('token')
def test_login_positive(token):
    response = requests.post(f'{api_url}login', json=POSITIVE_API_CREDS)
    print(response.json())
    assert response.json().split(' ')[0] == "Auth_token:"
    assert response.status_code == HTTPStatus.OK


@pytest.mark.parametrize('data', NEGATIVE_API_CREDS,
    ids=[
        "empty user", "empty password"])
def test_login_negative(token, data):
    response = requests.post(f'{api_url}login', json=data)
    print(response.json())
    assert response.json()['errorMessage'] == "Wrong password."
    assert response.status_code == HTTPStatus.OK


@pytest.mark.usefixtures('token')
def test_check(token):
    data = {"token": f'{token}'}
    response = requests.post(f'{api_url}check', json=data)
    assert response.json()['Item']['username'] == 'KateFox1'


def test_entries():
    response = requests.get(f'{api_url}entries')
    items = response.json()['Items']
    assert response.status_code == HTTPStatus.OK
    for item in items:
        assert len(item) == 6
