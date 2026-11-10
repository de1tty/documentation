#ФИО: Печёнкина Анастасия Антоновна
#Дата: 2026-11-09
#Время: 15:16
#Описание: Я скопировала код из примера теста который проверяет содержит ли заголовок подстроку,
#кликает по ссылке с названием "начать" и проверяет есть ли в заголовке страницы подстрока
#"Instalation"
import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # ожидаем заголовок содержащий подстроку
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # нажимаем на ссылку "Начать"
    page.get_by_role("link", name="Get started").click()

    # Ожидаем страницуу с заголовком Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()