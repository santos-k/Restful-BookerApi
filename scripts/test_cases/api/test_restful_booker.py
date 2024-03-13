import json

import pytest

from scripts.lib.api.restful_booker import *


class TestRestfulBookerAPI:
    logger.info('\n\n')
    logger.info(f"Test Suite: Restful Booker App APIs")

    def test_read_all_booking_ids(self):
        logger.info('\n')
        logger.info(f"Test Case: {(TestRestfulBookerAPI.test_read_all_booking_ids.__name__.replace('_', ' ').title())}")
        get_all_booking_ids()

    @pytest.mark.parametrize('booking_id', [124])
    def test_read_single_booking_id_details(self, booking_id):
        logger.info('\n')
        logger.info(
            f"Test Case: {(TestRestfulBookerAPI.test_read_single_booking_id_details.__name__.replace('_', ' ').title())}")
        get_single_booking_details(booking_id)

    def test_create_new_booking(self):
        logger.info('\n')
        logger.info(f"Test Case: {(TestRestfulBookerAPI.test_create_new_booking.__name__.replace('_', ' ').title())}")
        payload = json.dumps({
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        })
        headers = {
            'Content-Type': 'application/json'
        }

        create_new_booking(headers, payload)

