#ФИО: Печёнкина Анастасия Антоновна
#Дата: 2026-11-09
#Время: 15:16
#Описание: Я скопировала код из примера теста который проверяет содержит ли заголовок подстроку,
#кликает по ссылке с названием "начать" и проверяет есть ли в заголовке страницы подстрока
#"Instalation"
# я изменила ссылку, поменяв её на другой русский сайт, теперь код работает исправно
import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://www.python.org/")

    expect(page).to_have_title(re.compile("Welcome to Python.org"))

def test_get_started_link(page: Page):
    page.goto("https://www.python.org/")

    page.get_by_role("link", name="Getting Started").first.click()

    expect(page.get_by_role("heading", name="Python")).to_be_visible()