import pytest
import requests
import json
from helpers.authZ import obtain_token
from helpers.booking import has_booking_id

baseUrl = 'https://restful-booker.herokuapp.com/booking/'

# Booking - GetBookingIds


@pytest.mark.smoke
def test_get_booking_id_status_code():
    r = requests.get(baseUrl)
    assert r.status_code == 200


@pytest.mark.regression
def test_get_booking_param_first_name_valid():
    params = {
        "firstname": "Sally"
    }
    r = requests.get(baseUrl, params=params)
    body = r.json()
    flag = has_booking_id(body)
    assert flag == True


@pytest.mark.regression
def test_get_booking_param_first_name_not_existing():
    params = {
        "firstname": "Gonzalo"
    }
    r = requests.get(baseUrl, params=params)
    body = r.json()
    flag = has_booking_id(body)
    assert flag == False
