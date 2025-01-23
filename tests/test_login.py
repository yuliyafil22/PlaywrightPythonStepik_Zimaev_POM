# from pages.login_page import LoginPage
# from pages.dashboard_page import DashboardPage
# import pytest
#
# def test_login_failure(page):
#     login_page = LoginPage(page)
#     login_page.navigate()
#     login_page.login('invalid_user', 'invalid_password')
#     assert login_page.get_error_message() == 'Invalid credentials. Please try again.'
#
#
# #Создается объект DashboardPage.
# #Проверяется, что на странице отображается корректное приветственное сообщение.
#
# @pytest.mark.parametrize('username, password', [
#     ('user', 'user'),
#     ('admin', 'admin')
# ])
# def test_login_success(page):
#     login_page = LoginPage(page)
#     dashboard_page = DashboardPage(page)
#
#     login_page.navigate()
#     login_page.login('admin', 'admin')
#
#     dashboard_page.assert_welcome_message("Welcome admin")


import pytest
import allure


@allure.story('Login Feature')
@allure.title('Авторизаиця с недействительными учетными данными')
def test_login_failure(login_page):
    login_page.navigate()
    login_page.login('user', 'password')

    assert login_page.get_error_message() == 'Invalid credentials. Please try again.'


@pytest.mark.parametrize('username, password', [
    ('user', 'user'),
    ('admin', 'admin')
])

@allure.story('Login Feature')
@allure.title('Авторизаиця с корректными учетными данными')
def test_login_success(login_page, dashboard_page, username, password):
    login_page.navigate()
    login_page.login(username,password)
    dashboard_page.assert_welcome_message(f"Welcome {username}")

#test first branch
