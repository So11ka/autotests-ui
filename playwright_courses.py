from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.fill("user.name@gmail.com")

    registration_username_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_username_input.fill("username")

    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password_input.fill("password")

    registration_button = page.get_by_test_id("registration-page-registration-button")
    registration_button.click()

    context.storage_state(path='browser-state.json')

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text('Courses')

    courses_icon_folder = page.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_icon_folder).to_be_visible()

    there_is_no_results = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(there_is_no_results).to_be_visible()
    expect(there_is_no_results).to_have_text('There is no results')

    results_from_the_load_test_pipeline_will_be_displayed_here = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(results_from_the_load_test_pipeline_will_be_displayed_here).to_be_visible()
    expect(results_from_the_load_test_pipeline_will_be_displayed_here).to_have_text('Results from the load test pipeline will be displayed here')

