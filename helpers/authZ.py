import requests
import json

baseUrl = 'https://restful-booker.herokuapp.com/'


def obtain_token(userName, password):
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        'username': userName,
        'password': password
    }
    r = requests.post(baseUrl + 'auth', headers=headers,
                      data=json.dumps(payload))
    if r.status_code == 200:
        return r.json().get('token')
    else:
        raise Exception(
            f'Failed to obtain auth token. Status code obtained is: {r.status_code}')
