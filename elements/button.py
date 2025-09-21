from playwright.sync_api import expect
from elements.base_element import BaseElement


class Button(BaseElement):
    def check_enabled(self, index: int = 0, **kwargs):
        locator = self.get_locator(index, **kwargs)
        expect(locator).to_be_enabled()

    def check_disabled(self, index: int = 0, **kwargs):
        locator = self.get_locator(index, **kwargs)
        expect(locator).to_be_disabled()