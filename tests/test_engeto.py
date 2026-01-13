from playwright.sync_api import Page, expect


def test_homepage_title(open_homepage: Page):
    expect(open_homepage).to_have_title(
        "Kurzy programování a dalších IT technologií | ENGETO"
    )


def test_courses_link_visible(open_homepage: Page):
    courses_link = open_homepage.get_by_role("link", name="Kurzy", exact=True)
    expect(courses_link).to_be_visible()


def test_courses_link_navigation(open_homepage: Page):
    courses_link = open_homepage.get_by_role("link", name="Kurzy", exact=True)
    courses_link.click()
    expect(open_homepage).to_have_url("https://engeto.cz/prehled-kurzu/")


def test_footer_exists(open_homepage: Page):
    footer = open_homepage.locator("footer")
    expect(footer).to_be_visible()
