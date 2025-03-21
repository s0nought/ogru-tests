import pytest
from util.env import get_user_login, get_user_password
from playwright.sync_api import Page
from pages.home import HomePage

@pytest.fixture
def home_page(page: Page) -> HomePage:
    return HomePage(page)

@pytest.fixture
def user_login() -> str:
    return get_user_login()

@pytest.fixture
def user_password() -> str:
    return get_user_password()
