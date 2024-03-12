from scripts.lib.common.api_methods import APIMethod
from scripts.lib.common.logging import GenerateLog
from scripts.lib.common.assertion import Assertion

base_url = "https://restful-booker.herokuapp.com"
get_bookingIDs_endpoint = "booking"
get_bookingID_endpoint = 'booking/{}'
logger = GenerateLog.generate_log()


booker_api = APIMethod(base_url, logger)


def get_all_booking_ids():
    response = booker_api.get(get_bookingIDs_endpoint)
    if response:
        actual_status = response.status_code
        response_json_data = response.json()
        expected_status = 200
        Assertion.assert_equal(actual_status, expected_status, logger)
        Assertion.assert_in('bookingid', response_json_data[0], logger)


def get_single_booking_details(booking_id):
    response = booker_api.get(get_bookingIDs_endpoint, booking_id)
    if response:
        actual_status = response.status_code
        response_json_data = response.json()
        expected_status = 200
        Assertion.assert_equal(actual_status, expected_status, logger)
        for key in ['firstname', 'lastname', 'totalprice', 'depositpaid', 'bookingdates', 'additionalneeds']:
            Assertion.assert_in(key, response_json_data, logger, f'{key} not in data')
