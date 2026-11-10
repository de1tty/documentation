#ФИО: Печёнкина Анастасия Антоновна
#Дата: 2026-11-09
#Время: 16:48
#Описание: фикстура с обастью видимости autouse ведет себя как beforeEach/afterEach
#мы создаем фикстуру, которая перед каждым тестом возвращается по первоначальной
#ссылке,а в утвержденях она ожидает страницу с указаным URL
import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):

    print("before the test runs")

    # идет на первоначальную ссылку пред каждым тестом
    page.goto("https://playwright.dev/")
    yield

    print("after the test runs")

def test_main_navigation(page: Page):
    # в утверждениях ожидают API
    expect(page).to_have_url("https://playwright.dev/")