from playwright.sync_api import Page
from util.path import get_path
from util.json import load

class CustomComponent:
    def __init__(self, page: Page, parent_name: str, elements_dir: str):
        self.page = page
        self.parent_name = parent_name
        self.class_name = self.__class__.__name__
        self.element_parent = f"{self.parent_name} - {self.class_name}"
        self.elements: dict = load(get_path("components", elements_dir, "elements.json"))
