from lesson_29.components.product_card import ProductCard


class CatalogPage:

    PRODUCT_CARD = ".catalogCard-box.j-product-container"

    def __init__(self, page):
        self.page = page

    @property
    def cards(self):
        return self.page.locator(self.PRODUCT_CARD)

    def get_product(self, index):
        return ProductCard(
            self.cards.nth(index)
        )

    def get_all_products(self):
        count = self.cards.count()

        return [
            ProductCard(self.cards.nth(i))
            for i in range(count)
        ]

    def get_product_by_title(self, title):

        for product in self.get_all_products():

            if product.title == title:
                return product

        raise Exception(
            f"{title} не знайдено"
        )


