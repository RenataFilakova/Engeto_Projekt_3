import pytest
from playwright.sync_api import Page

BASE_URL = "https://engeto.cz"

COOKIE_BUTTON_NAMES = [
    "Souhlasím",
    "Přijmout vše",
    "Přijmout všechny",
    "Accept all",
    "Accept All",
    "I agree",
    "Rozumím",
]


def handle_cookie_banner(page: Page) -> None:
    try:
        for name in COOKIE_BUTTON_NAMES:
            button = page.get_by_role("button", name=name)
            if button.first.is_visible():
                button.first.click()
                return

        for frame in page.frames:
            for name in COOKIE_BUTTON_NAMES:
                button = frame.get_by_role("button", name=name)
                if button.first.is_visible():
                    button.first.click()
                    return

    except Exception:
        pass


@pytest.fixture
def open_homepage(page: Page) -> Page:
    page.goto(BASE_URL)
    handle_cookie_banner(page)
    return page
