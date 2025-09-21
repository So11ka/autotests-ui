from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.button import Button


class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.button = Button(page, 'course-view-menu-button', 'Button menu')
        self.delete_button = Button(page,'course-view-delete-menu-item', 'Delete course')
        self.edit_button = Button(page,'course-view-edit-menu-item', 'Edit course')

    def click_edit(self, index: int):
        self.button.check_visible(index=index)
        self.button.click(index=index)

        self.edit_button.check_visible(index=index)
        self.edit_button.click(index=index)

    def click_delete(self, index: int):
        self.button.check_visible(index=index)
        self.button.click(index=index)

        self.delete_button.check_visible(index=index)
        self.delete_button.click(index=index)