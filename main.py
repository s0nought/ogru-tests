import logging
import pytest
import sys
import util.allure
import util.env

logger = logging.getLogger(__name__)

LOG_FILE = "main.log"
LOG_FORMAT = r"[%(asctime)s] %(levelname)s :: %(filename)s :: %(funcName)s :: %(message)s"
LOGGING_LEVEL = util.env.get_logging_level()

def main() -> None:
    logging.basicConfig(filename=LOG_FILE, format=LOG_FORMAT, level=LOGGING_LEVEL)
    logger.info("RUNNING MAIN SEQUENCE")

    util.allure.clean_results()
    pytest.main(sys.argv[1:])
    util.allure.copy_history()
    util.allure.write_environment_file()
    util.allure.generate_report()
    util.allure.open_report()

    logger.info("DONE")

if __name__ == "__main__":
    main()
