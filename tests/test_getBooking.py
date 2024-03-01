import pytest
import requests

baseUrl = 'https://restful-booker.herokuapp.com/booking/'

# GetBooking


@pytest.mark.smoke
def test_get_booking_id_status_code():
    id = '1'
    r = requests.get(baseUrl + id)
    assert r.status_code == 200


@pytest.mark.regression
def test_get_booking_id_not_existing():
    id = '9999999999999999'
    r = requests.get(baseUrl + id)
    assert r.status_code == 404
