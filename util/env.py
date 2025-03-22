from dotenv import load_dotenv
from os import getenv

load_dotenv()

def get_ci() -> str:
    return getenv("CI")

def get_logging_level() -> str:
    return getenv("OGRU_LOGGING_LEVEL", "INFO")

def get_user_login() -> str:
    return getenv("OGRU_USER_LOGIN", "N/A")

def get_user_password() -> str:
    return getenv("OGRU_USER_PASSWORD", "N/A")

def get_allure_results() -> str:
    return getenv("OGRU_ALLURE_RESULTS", "allure-results")

def get_allure_report() -> str:
    return getenv("OGRU_ALLURE_REPORT", "allure-report")

def get_allure_environment_file() -> str:
    return getenv("OGRU_ALLURE_ENVIRONMENT_FILE", "environment.properties")

def get_pytest_addopts() -> str:
    return getenv("PYTEST_ADDOPTS", "N/A")
