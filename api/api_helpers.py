import base64
from json import JSONDecodeError
from typing import Dict, Union
from http import HTTPStatus
import requests
from Links import api_url
from constants import POSITIVE_API_CREDS


def get_token():
    response = requests.post(f'{api_url}login', json=POSITIVE_API_CREDS)
    token = response.json().split(' ')[1]
    return token


# print(get_token)

