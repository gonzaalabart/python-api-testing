import pytest
import requests

baseUrl = 'https://restful-booker.herokuapp.com/'


@pytest.mark.smoke
@pytest.mark.regression
def test_health_check():
    r = requests.get(baseUrl + 'ping')
    assert r.status_code == 201
