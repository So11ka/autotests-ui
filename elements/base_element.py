from playwright.sync_api import Page, Locator, expect


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.name = name
        self.locator = locator

    def get_locator(self, index: int = 0, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        return self.page.get_by_test_id(locator).nth(index)

    def click(self, index: int = 0, **kwargs):
        locator = self.get_locator(index, **kwargs)
        locator.click()

    def check_visible(self, index: int = 0, **kwargs):
        locator = self.get_locator(index, **kwargs)
        expect(locator).to_be_visible()

    def check_have_text(self, text: str, index: int = 0, **kwargs):
        locator = self.get_locator(index, **kwargs)
        expect(locator).to_have_text(text)
