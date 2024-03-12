class Assertion:
    @staticmethod
    def _log_and_assert(result, logger, msg=""):
        if result:
            logger.info("Test Result: PASSED")
            assert True
        else:
            logger.warning("Test Result: FAILED")
            assert False, msg

    @staticmethod
    def assert_equal(actual_value, expected_value, logger, msg=""):
        logger.info(f"Actual Value: {actual_value}, Expected Value: {expected_value}")
        Assertion._log_and_assert(actual_value == expected_value, logger, msg)

    @staticmethod
    def assert_not_equal(actual_value, expected_value, logger, msg=""):
        logger.info(f"Actual Value: {actual_value}, Expected Value: {expected_value}")
        Assertion._log_and_assert(actual_value != expected_value, logger, msg)

    @staticmethod
    def assert_in(member, container, logger, msg=""):
        logger.info(f"Checking '{member}' presence in {container}")
        Assertion._log_and_assert(member in container, logger, msg)

    @staticmethod
    def asset_not_in(member, container, logger, msg=""):
        logger.info(f"Checking '{member}' presence in {container}")
        Assertion._log_and_assert(member not in container, logger, msg)

    @staticmethod
    def assert_true(result, msg=''):
        Assertion._log_and_assert(result, msg)

    @staticmethod
    def assert_false(result, logger, msg=''):
        if result:
            Assertion._log_and_assert(False, logger, msg)
        else:
            Assertion._log_and_assert(True, logger, msg)
