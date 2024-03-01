import pytest
import requests
import json
from helpers.authZ import obtain_token

baseUrl = 'https://restful-booker.herokuapp.com/'
headers = {
    'Content-Type': 'application/json'
}


@pytest.mark.smoke
def test_authZ_status_code():
    payload = {
        'username': 'admin',
        'password': 'password123'
    }
    r = requests.post(baseUrl + 'auth', headers=headers,
                      data=json.dumps(payload))
    assert r.status_code == 200


@pytest.mark.regression
def test_authZ_bad_credentials():
    payload = {
        'username': 'wrongUserName',
        'password': 'wrongPassword'
    }
    r = requests.post(baseUrl + 'auth', headers=headers,
                      data=json.dumps(payload))
    body = r.json()
    # I would use an status code 401, but this API always response with a 200, but it doesnt have the token in the body. But have a 'Bad credentials' message inside it.
    assert 'Bad credentials' in body['reason']
