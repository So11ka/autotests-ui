from playwright.sync_api import Page, expect
from components.base_component import BaseComponent


class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.button = page.get_by_test_id('course-view-menu-button')
        self.delete_button = page.get_by_test_id('course-view-delete-menu-item')
        self.edit_button = page.get_by_test_id('course-view-edit-menu-item')

    def click_edit(self, index: int):
        expect(self.button.nth(index)).to_be_visible()
        self.button.nth(index).click()

        expect(self.edit_button.nth(index)).to_be_visible()
        self.edit_button.nth(index).click()

    def click_delete(self, index: int):
        expect(self.button.nth(index)).to_be_visible()
        self.button.nth(index).click()

        expect(self.delete_button.nth(index)).to_be_visible()
        self.delete_button.nth(index).click()