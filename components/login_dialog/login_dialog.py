from playwright.sync_api import Page
from components.custom import CustomComponent
from elements.custom import CustomElement

class LoginDialog(CustomComponent):
    def __init__(self, page: Page, parent_name: str) -> None:
        super().__init__(page, parent_name)

        self.username_input = CustomElement(
            self.page,
            self.element_parent,
            self.elements_data.get("usernameInput")
        )
        self.password_input = CustomElement(
            self.page,
            self.element_parent,
            self.elements_data.get("passwordInput")
        )
        self.submit_button = CustomElement(
            self.page,
            self.element_parent,
            self.elements_data.get("submitButton")
        )

    def fill_username_input(self, value: str) -> None:
        self.username_input.fill(value)

    def fill_password_input(self, value: str) -> None:
        self.password_input.fill(value, is_masked=True)

    def click_submit_button(self) -> None:
        self.submit_button.click()
