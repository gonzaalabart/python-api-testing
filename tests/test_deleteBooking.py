import pytest
import requests
import json
from helpers.authZ import obtain_token
from helpers.booking import create_booking

baseUrl = 'https://restful-booker.herokuapp.com/booking/'

# In theory I would create a post, and then delete it. But the post is actually not created, so I cant delete it.


@pytest.mark.smoke
def test_delete_booking_status_code_200():
    token = obtain_token('admin', 'password123')
    bookingCreated = create_booking(baseUrl)
    body = bookingCreated.json()
    bookingId = str(body['bookingid'])
    headers = {
        'Content-Type': 'Application/json',
        # 'Authorization': f'Basic {token}'
    }
    r = requests.delete(baseUrl + bookingId, auth=('admin', 'password123'))
    assert r.status_code == 201
