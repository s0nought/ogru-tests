import allure
from playwright.sync_api import Page
from pages.custom import CustomPage

class HomePage(CustomPage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.page_path = "/"

    def navigate(self) -> None:
        with allure.step(self.get_step_title(f"Navigate to {self.page_path}")):
            self.page.goto(self.page_path)
