"""
Page Class класс должен содержать все элементы и методы, необходимые для взаимодействия с этой страницей.
 Этот класс служит обёрткой для взаимодействия с конкретной страницей.

Наша первая задача - создать класс, описывающий страницу входа в систему

"""

from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):  # это аннотация типа, указывающая, что параметр page должен быть объектом
        # типа Page из Playwright.
        self.page = page  # сохраняет переданный объект страницы в атрибуте экземпляра класса для дальнейшего использования.
        self.username_input = page.locator('#username')
        self.password_input = page.locator('#password')
        self.login_button = page.locator('#login')
        self.error_message = page.locator('#errorAlert')


    def navigate(self):  # Открывает страницу логина
        self.page.goto("https://zimaev.github.io/pom/")


    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()


    def get_error_message(self):
         return self.error_message.inner_text()

