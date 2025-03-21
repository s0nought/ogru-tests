import allure
from playwright.sync_api import Page, Locator, expect

class CustomElement:
    def __init__(self, page: Page, parent_name: str, props: dict[str, str]) -> None:
        self.page = page
        self.parent_name = parent_name
        self.description = props.get("description")
        self.selector = props.get("selector")

    def get_locator(self) -> Locator:
        return self.page.locator(self.selector)

    def get_step_title(self, title: str) -> str:
        return f"{self.parent_name} - {self.description} - {title}"

    def click(self) -> None:
        with allure.step(self.get_step_title("Click on")):
            self.get_locator().click()

    def fill(self, value: str, is_masked: bool = False) -> None:
        with allure.step(self.get_step_title(f"Fill with value \"{'***' if is_masked else value}\"")):
            self.get_locator().fill(value)

    def assert_not_visible(self) -> None:
        with allure.step(self.get_step_title("Assert not visible")):
            expect(self.get_locator()).not_to_be_visible()
