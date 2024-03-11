from scripts.lib.api.restful_booker import logger


class Assertion:
    @staticmethod
    def _log_and_assert(result, msg=""):
        if result:
            logger.info("Test Result: PASSED")
            assert True
        else:
            logger.warning("Test Result: FAILED")
            assert False, msg

    @staticmethod
    def assert_true(actual_value, expected_value, msg=""):
        logger.info(f"Actual Value: {actual_value}, Expected Value: {expected_value}")
        Assertion._log_and_assert(actual_value == expected_value, msg)

    @staticmethod
    def assert_false(actual_value, expected_value, msg=""):
        logger.info(f"Actual Value: {actual_value}, Expected Value: {expected_value}")
        Assertion._log_and_assert(actual_value != expected_value, msg)

    @staticmethod
    def assert_in(member, container, msg=""):
        Assertion._log_and_assert(member in container, msg)

    @staticmethod
    def asset_not_in(member, container, msg=""):
        Assertion._log_and_assert(member not in container, msg)
