import pytest

from api.api_methods import login
from api.api_methods import get_token, check_auth
from constants import POSITIVE_API_CREDS, NEGATIVE_API_CREDS


@pytest.fixture()
def token():
    return get_token()


def test_login_positive():
    text = login(credentials=POSITIVE_API_CREDS)
    assert 'Auth_token' in text


def test_check_authorization(token):
    check_auth(token=token)


@pytest.mark.parametrize('data', NEGATIVE_API_CREDS, ids=["empty user", "empty password", "wrong data"])
def test_login_negative(data):
    text = login(credentials=NEGATIVE_API_CREDS)
    assert 'errorMessage' in text
