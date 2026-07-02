import os
import pytest

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

from lesson_29.pages.login_page import LoginPage


load_dotenv()

BASE_URL = "https://shos.com.ua/"
AUTH_FILE = "auth.json"

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="session", autouse=True)
def save_auth(browser):

    context = browser.new_context()
    page = context.new_page()

    login = LoginPage(page)

    login.authorize(
        os.getenv("SHOS_EMAIL"),
        os.getenv("SHOS_PASSWORD")
    )

    context.storage_state(path=AUTH_FILE)
    context.close()


@pytest.fixture
def logged_in_page(browser):

    context = browser.new_context(
        storage_state=AUTH_FILE
    )

    page = context.new_page()
    page.goto(BASE_URL)
    yield page
    context.close()

