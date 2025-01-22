import pytest
import allure


@allure.story('Login Feature')
@allure.title('Авторизаиця с недействительными учетными данными')
def test_login_failure(login_page):
    login_page.navigate()
    login_page.login('user', 'password')