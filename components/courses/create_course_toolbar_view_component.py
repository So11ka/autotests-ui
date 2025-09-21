import re
from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'create-course-toolbar-title-text', 'Title')
        self.create_course_button = Button(page, 'create-course-toolbar-create-course-button', 'Create Course')

    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text('Create course')

        self.create_course_button.check_visible()

    def check_disabled_create_course_button(self):
        self.create_course_button.check_disabled()

    def click_create_course_button(self):
        self.create_course_button.check_enabled()
        self.create_course_button.click()

        self.check_current_url(re.compile('.*/#/courses'))