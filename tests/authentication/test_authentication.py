import allure
import pytest
from pages.home import HomePage

@pytest.mark.cjm
@allure.epic("UI")
@allure.feature("Core")
@allure.story("Authentication")
@allure.title("Authentication")
def test_authentication(home_page: HomePage, user_login: str, user_password: str) -> None:
    home_page.navigate()
    home_page.interact_header().click_login_link()
    home_page.interact_login_dialog().fill_username_input(user_login)
    home_page.interact_login_dialog().fill_password_input(user_password)
    home_page.interact_login_dialog().click_submit_button()
    home_page.interact_header().assert_login_link_not_visible()
