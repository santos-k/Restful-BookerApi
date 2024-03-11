import requests

from scripts.lib.common.api_methods import APIMethod
from scripts.lib.common.logging import GenerateLog

base_url = "https://restful-booker.herokuapp.com"
get_bookingIDs_endpoint = "booking"
get_bookingID_endpoint = 'booking/{}'
logger = GenerateLog.generate_log()


booker_api = APIMethod(base_url, logger)


def get_all_booking_ids():
    response = booker_api.get(get_bookingIDs_endpoint)
    if response:
        expected_status = 200
        logger.info(f"Actual Status Code: {response.status_code}, Expected Status Code: {expected_status}")
        # logger.info(f"Response Body: {response.json()}")


get_all_booking_ids()
