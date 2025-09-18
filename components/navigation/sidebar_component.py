import re
from playwright.sync_api import Page
from components.base_components import BaseComponent
from components.navigation.sidebar_list_item_component import Sidebar_List_Item_Component


class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.logout_list_item = Sidebar_List_Item_Component(page, 'logout')
        self.dashboard_list_item = Sidebar_List_Item_Component(page, 'dashboard')
        self.courses_list_item = Sidebar_List_Item_Component(page, 'courses')

    def check_visible(self):
        self.logout_list_item.check_visible('Logout')
        self.dashboard_list_item.check_visible('Dashboard')
        self.courses_list_item.check_visible('Courses')

    def click_logout(self):
        self.logout_list_item.navigate(re.compile(r".*/#/auth/login"))

    def click_courses(self):
        self.courses_list_item.navigate(re.compile(r".*/#/courses"))

    def click_dashboard(self):
        self.dashboard_list_item.navigate(re.compile(r".*/#/dashboard"))