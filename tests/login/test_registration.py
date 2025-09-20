from pytest import mark
from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage


@mark.regression
@mark.ui
@mark.registration
class TestRegistration:
    def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.registration_form.fill("username@gmail.com", "username", "password")
        registration_page.registration_form.check_visible("username@gmail.com", "username", "password")
        registration_page.click_registration_button()

        dashboard_page.toolbar_dashboard_view.check_visible()