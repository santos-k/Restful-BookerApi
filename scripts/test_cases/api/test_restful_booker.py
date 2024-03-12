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
        logger.info(f"Test Case: {(TestRestfulBookerAPI.test_read_single_booking_id_details.__name__.replace('_', ' ').title())}")
        get_single_booking_details(booking_id)

