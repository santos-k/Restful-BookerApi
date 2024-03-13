from scripts.lib.common.api_methods import APIMethod
from scripts.lib.common.logging import GenerateLog
from scripts.lib.common.assertion import Assertion

base_url = "https://restful-booker.herokuapp.com"
get_bookingID_endpoint = "booking"
logger = GenerateLog.generate_log()


booker_api = APIMethod(base_url, logger)


def get_all_booking_ids():
    response = booker_api.get(get_bookingID_endpoint)
    actual_status = response.status_code
    expected_status = 200
    Assertion.assert_equal(actual_status, expected_status, logger)
    if actual_status == expected_status:
        response_json_data = response.json()
        Assertion.assert_in('bookingid', response_json_data[0], logger)


def get_single_booking_details(booking_id):
    response = booker_api.get(get_bookingID_endpoint, booking_id)
    actual_status = response.status_code
    expected_status = 200
    Assertion.assert_equal(actual_status, expected_status, logger)
    if actual_status == expected_status:
        response_json_data = response.json()
        for key in ['firstname', 'lastname', 'totalprice', 'depositpaid', 'bookingdates', 'additionalneeds']:
            Assertion.assert_in(key, response_json_data, logger, f'{key} not in data')


def create_new_booking(headers, payload):
    response = booker_api.post(headers, payload, get_bookingID_endpoint)
    actual_status = response.status_code
    expected_code = 200
    Assertion.assert_equal(actual_status, expected_code, logger)
    if actual_status == expected_code:
        json_data = response.json()
        for key in ['bookingid', 'booking']:
            Assertion.assert_in(key, json_data, logger)

        for booking_key in ['firstname', 'lastname', 'totalprice', 'depositpaid', 'bookingdates', 'additionalneeds']:
            Assertion.assert_in(booking_key, json_data['booking'], logger)
