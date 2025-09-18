from pytest import fixture
from playwright.sync_api import Page
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


@fixture
def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(chromium_page)

@fixture
def registration_page(chromium_page: Page) -> RegistrationPage:
    return RegistrationPage(chromium_page)

@fixture
def dashboard_page(chromium_page: Page) -> DashboardPage:
    return DashboardPage(chromium_page)

@fixture
def courses_list_page(chromium_page: Page) -> CoursesListPage:
    return CoursesListPage(chromium_page)

@fixture
def create_course_page(chromium_page: Page) -> CreateCoursePage:
    return CreateCoursePage(chromium_page)


"""
Почему registration_page.page и dashboard_page.page — это один и тот же объект?

Всё дело в том, как устроены фикстуры в тесте.

Когда вы пишете:

def test_successful_registration(
    registration_page: RegistrationPage,
    dashboard_page: DashboardPage,
):
    
оба объекта RegistrationPage и DashboardPage создаются с помощью одной и той же фикстуры chromium_page. То есть даже если страницы две, внутри них объекты page одинаковые!

И это работает так:

При запуске каждого теста создаётся один браузер, в нём один контекст, и одна вкладка (Page).
Именно этот один Page передаётся во все POM-объекты в рамках одного теста.
Что происходит внутри Page Object 

Посмотрите, как устроен POM:

class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page

                  
И аналогично у DashboardPage.

Когда pytest собирает зависимости теста, он сначала вызовет фикстуру chromium_page, создаст браузер и вкладку, а потом передаст одну и ту же вкладку в оба объекта:

registration_page = RegistrationPage(page)
dashboard_page = DashboardPage(page)

                  
Это значит, что:

registration_page.page is dashboard_page.page  # True
  
Что это означает на практике?

Если registration_page вызывает visit() или нажимает кнопку, происходит навигация во вкладке. А dashboard_page тут же "видит" ту же самую вкладку и тот же самый URL!

Пример:

registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course//registration")
print(dashboard_page.page.url)  # => тоже будет https://nikita-filonov.github.io/qa-automation-engineer-ui-course//registration

                
Потому что у них общий .page.

Зачем так сделано?

Это специальный подход, чтобы:

Один тест моделировал действия одного пользователя в одном браузере.
Каждый POM отвечал за отдельный экран или часть UI, но работал в общей среде.
Не было путаницы, что у одного браузера вдруг два разных состояния.
Что было бы, если POM-объекты имели разные page?

Тогда у вас открывалось бы по вкладке на каждый экран, и вы не могли бы, например, проверить корректность перехода от одной страницы к другой. Это дало бы ложную изоляцию и исказило бы логику взаимодействия.

Вывод

Ваш пример с print(...) вполне логичен и хорошо демонстрирует, что page действительно один на весь тест.

А visit() внутри второго POM-а может скрыть ошибку перехода, если вдруг редирект не произошёл — именно поэтому я и указывал в рецензии, что делать это не стоит.
"""