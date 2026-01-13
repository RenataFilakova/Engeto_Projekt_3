from playwright.sync_api import Page


def test_homepage_title(page: Page):
    page.goto("https://engeto.cz")
    assert "ENGETO" in page.title()


def test_courses_link_visible(page: Page):
    page.goto("https://engeto.cz")
    courses_link = page.get_by_role("link", name="Kurzy", exact=True)
    assert courses_link.is_visible()


def test_footer_exists(page: Page):
    page.goto("https://engeto.cz")
    footer = page.locator("footer")
    assert footer.is_visible()
