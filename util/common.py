from pytest import __version__ as pytest_version
from platform import python_version, system

def get_pytest_version() -> str:
    return pytest_version

def get_python_version() -> str:
    return python_version()

def get_system_name() -> str:
    return system()
