import pytest
import requests
import json

baseUrl = 'https://restful-booker.herokuapp.com/booking'


@pytest.mark.smoke
def test_create_booking_status_code():
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    headers = {
        'Content-Type': 'application/json'
    }
    r = requests.post(baseUrl, headers=headers,
                      data=json.dumps(payload))
    assert r.status_code == 200


@pytest.mark.regression
def test_create_booking_without_adittionalneeds():
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    r = requests.post(baseUrl, headers=headers,
                      data=json.dumps(payload))
    assert r.status_code == 200


@pytest.mark.regression
def test_create_booking_without_data_500():
    payload = {
        "firstname": "",
        "lastname": "",
        "totalprice": None,
        "depositpaid": None,
        "bookingdates": {
            "checkin": "",
            "checkout": ""
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    r = requests.post(baseUrl, headers=headers,
                      data=json.dumps(payload))
    assert r.status_code == 500


def test_create_booking_checkout_later_than_checkin():
    payload = {
        "firstname": "",
        "lastname": "",
        "totalprice": None,
        "depositpaid": None,
        "bookingdates": {
            "checkin": "",
            "checkout": ""
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    r = requests.post(baseUrl, headers=headers,
                      data=json.dumps(payload))
