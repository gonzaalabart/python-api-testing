import pytest
import requests
import json


def has_booking_id(body):
    for item in body:
        if "bookingid" in item:
            return True
    return False


def create_booking(baseUrl):
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
    return r
