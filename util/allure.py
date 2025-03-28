import logging
import subprocess
import util.common
import util.dir
import util.env
import util.file
import util.path
from pathlib import Path, PurePath

logger = logging.getLogger(__name__)

results_name = util.env.get_allure_results()
report_name = util.env.get_allure_report()
environment_file_name = util.env.get_allure_environment_file()

results = util.path.get_path(results_name)
report = util.path.get_path(report_name)
environment_file = util.path.get_path(results_name, environment_file_name)

results_history = util.path.get_pure_path(results_name, "history")
report_history = util.path.get_pure_path(report_name, "history")

def copy_history(report_history: PurePath = report_history, results_history: PurePath = results_history) -> None:
    try:
        logger.debug(f"Src: {report_history}")
        logger.debug(f"Dst: {results_history}")
        util.dir.copy(report_history, results_history)
    except FileNotFoundError as e:
        logger.warning(e)

    logger.info("OK")

def get_environment_file_content() -> str:
    content = "system_name={0}\npython_version={1}\npytest_version={2}\npytest_addopts={3}".format(
        util.common.get_system_name(),
        util.common.get_python_version(),
        util.common.get_pytest_version(),
        util.env.get_pytest_addopts(),
    )

    logger.debug(f"Content: {content.replace('\n', ' ')}")
    logger.info("OK")

    return content

def write_environment_file(file: Path = environment_file) -> None:
    util.file.write(file=file, content=get_environment_file_content())

    logger.info("OK")

def generate_report(path: str = results_name) -> None:
    cmd = ["allure", "generate", "--clean", path]
    logger.debug(f"Command: {cmd}")

    p = subprocess.run(cmd, shell=True)
    logger.debug(f"Exit code: {p.returncode}")

    logger.info("OK")

def open_report(path: str = report_name) -> None:
    cmd = ["allure", "open", path]
    logger.debug(f"Command: {cmd}")

    subprocess.Popen(cmd, shell=True)

    logger.info("OK")
