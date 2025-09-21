from playwright.sync_api import Locator, expect
from elements.base_element import BaseElement


class Input(BaseElement):
    def get_locator(self, index: int = 0, **kwargs) -> Locator:
        return super().get_locator(index, **kwargs).locator('input')

    def fill(self, value: str, index: int = 0, **kwargs):
        locator = self.get_locator(index, **kwargs)
        locator.fill(value)

    def check_have_value(self, value: str, index: int = 0, **kwargs):
        locator = self.get_locator(index, **kwargs)
        expect(locator).to_have_value(value)

