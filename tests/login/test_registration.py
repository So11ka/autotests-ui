from pytest import mark
from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage


@mark.regression
@mark.ui
@mark.registration
class TestRegistration:
    def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.fill_registration_form("username@gmail.com", "username", "password")
        registration_page.click_registration_button()

        dashboard_page.check_visible_dashboard_title()