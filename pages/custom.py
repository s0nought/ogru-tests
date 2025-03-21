from playwright.sync_api import Page
from components.header.header import Header
from components.login_dialog.login_dialog import LoginDialog

class CustomPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.class_name = self.__class__.__name__
        self.header = Header(self.page, self.class_name)
        self.login_dialog = LoginDialog(self.page, self.class_name)

    def get_step_title(self, title: str) -> str:
        return f"{self.class_name} - {title}"

    def interact_header(self) -> Header:
        return self.header

    def interact_login_dialog(self) -> LoginDialog:
        return self.login_dialog
