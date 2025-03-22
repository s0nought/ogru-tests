import logging
import pytest
import sys
import util.allure
import util.env

logger = logging.getLogger(__name__)

LOG_FILE = "main.log"
LOG_FORMAT = r"[%(asctime)s] %(levelname)s :: %(filename)s :: %(funcName)s :: %(message)s"
LOGGING_LEVEL = util.env.get_logging_level()
CI = util.env.get_ci()

def main() -> None:
    logging.basicConfig(filename=LOG_FILE, format=LOG_FORMAT, level=LOGGING_LEVEL)
    logger.info("RUNNING MAIN SEQUENCE")

    if CI == None:
        util.allure.clean_results()

    pytest.main(sys.argv[1:])

    if CI == None:
        util.allure.copy_history()

    util.allure.write_environment_file()

    if CI == None:
        util.allure.generate_report()
        util.allure.open_report()

    logger.info("DONE")

if __name__ == "__main__":
    main()
