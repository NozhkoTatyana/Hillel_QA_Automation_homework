from playwright.sync_api import Locator


class ProductCard:

    TITLE = ".catalogCard-title"
    ARTICLE = ".catalogCard-code"
    PRICE = ".catalogCard-price"

    def __init__(self, card: Locator):
        self.card = card
        self.product_id = self.card.get_attribute("data-id")
        self.buy_button = card.locator(
            f"#j-buy-button-widget-{self.product_id}"
        )

    @property
    def title(self):
        return self.card.locator(self.TITLE).inner_text()

    @property
    def article(self):
        return self.card.locator(self.ARTICLE).inner_text()

    @property
    def price(self):
        return self.card.locator(self.PRICE).inner_text()

    @property
    def is_buy_button_visible(self) -> bool:
        return self.buy_button.is_visible()

    def add_to_cart(self):
        self.buy_button.scroll_into_view_if_needed()
        self.buy_button.click()