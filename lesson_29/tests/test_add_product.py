from lesson_29.components.menu_component import MenuComponent
from lesson_29.pages.catalog_page  import CatalogPage
from lesson_29.pages.home_page import HomePage
from playwright.sync_api import expect
import pytest

WANTED_PRODUCT_1 = "Жувальна гумка Otdushi Made Успіхоактивізін верде"
WANTED_PRODUCT_2 = "Жувальна гумка Otdushi Made Антистрес форте"

#@pytest.mark.skip
def test_add_from_catalog(logged_in_page):

    logged_in_page.goto("https://shos.com.ua/zhuiky/")
    catalog = CatalogPage(logged_in_page)

    product = catalog.get_product_by_title(WANTED_PRODUCT_1)

    assert product.is_buy_button_visible, (
        f"Товар '{WANTED_PRODUCT_1}' не знайдено"
    )

    product.add_to_cart()
    expect(product.buy_button).not_to_have_class("__disabled")
    badge = logged_in_page.locator(".basket__items.j-basket-quantity")
    expect(badge).to_contain_text("2")


def test_add_from_home_flow(logged_in_page):
    home_page = HomePage(logged_in_page)
    menu = MenuComponent(logged_in_page)
    home_page.open()
    menu.open_subcategory("Ігри","Головоломки")
    expect(logged_in_page).to_have_url("https://shos.com.ua/holovolomky/")

    catalog = CatalogPage(logged_in_page)
    product = catalog.get_all_products()[0]

    assert product.is_buy_button_visible

    product.add_to_cart()





