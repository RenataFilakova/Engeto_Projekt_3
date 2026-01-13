import pytest
from playwright.sync_api import Page

BASE_URL = "https://engeto.cz"

@pytest.fixture
def open_homepage(page: Page) -> Page:
    page.goto(BASE_URL)

    # cookie banner – pokud se objeví, zkus ho zavřít
    try:
        accept_button = page.get_by_role("button", name="Souhlasím")
        if accept_button.is_visible():
            accept_button.click()
    except Exception:
        pass

    return page
