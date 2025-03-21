from playwright.sync_api import Page
from components.custom import CustomComponent
from elements.custom import CustomElement

class Header(CustomComponent):
    def __init__(self, page: Page, parent_name: str) -> None:
        super().__init__(page, parent_name, "header")

        self.login_link = CustomElement(
            self.page,
            self.element_parent,
            self.elements.get("loginLink"),
        )

    def click_login_link(self) -> None:
        self.login_link.click()

    def assert_login_link_not_visible(self) -> None:
        self.login_link.assert_not_visible()
