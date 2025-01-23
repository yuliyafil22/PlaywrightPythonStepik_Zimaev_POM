"""Создадим Page Class для страницы панели управления, которая появляется после успешного входа."""

from playwright.sync_api import Page, expect

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.profile = page.locator('#usernameDisplay')
        self.logout = page.locator('#logout') #инициализируют локаторы для элементов страницы, используя метод locator

#проверяет текст приветственного сообщения на панели управления
    def assert_welcome_message(self, message):
        expect(self.profile).to_have_text(message)
