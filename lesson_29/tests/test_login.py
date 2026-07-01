from lesson_29.components.user_menu import UserMenuComponent
from playwright.sync_api import expect
import  pytest


@pytest.mark.skip
def test_login(logged_in_page):
    userbar = UserMenuComponent(logged_in_page)
    userbar.open()
    expect(logged_in_page.get_by_text("Особисті дані")).to_be_visible()