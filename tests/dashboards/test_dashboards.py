from pages.dashboard_page import DashboardPage
from pytest import mark

@mark.dashboard
@mark.ui
@mark.regression
class TestDashboard():
    def test_dashboard_displaying(self, dashboard_page: DashboardPage):
        dashboard_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
        dashboard_page.navbar.check_visible('username')
        dashboard_page.check_visible_dashboard_title()
        dashboard_page.check_visible_activities_chart()
        dashboard_page.check_visible_scores_chart()
        dashboard_page.check_visible_courses_chart()
        dashboard_page.check_visible_students_chart()


