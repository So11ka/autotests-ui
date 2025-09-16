from playwright.sync_api import sync_playwright, expect, Page
from pytest import mark

@mark.regression
@mark.ui
@mark.courses
class TestCourses:
    def test_empty_courses_list(self, chromium_page_with_state: Page):
        chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        courses_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text('Courses')

        courses_icon_folder = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
        expect(courses_icon_folder).to_be_visible()

        there_is_no_results = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
        expect(there_is_no_results).to_be_visible()
        expect(there_is_no_results).to_have_text('There is no results')

        results_from_the_load_test_pipeline_will_be_displayed_here = chromium_page_with_state.get_by_test_id(
            'courses-list-empty-view-description-text')
        expect(results_from_the_load_test_pipeline_will_be_displayed_here).to_be_visible()
        expect(results_from_the_load_test_pipeline_will_be_displayed_here).to_have_text(
            'Results from the load test pipeline will be displayed here')

        chromium_page_with_state.wait_for_timeout(5000)