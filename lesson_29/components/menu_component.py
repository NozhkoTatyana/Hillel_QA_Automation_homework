

class MenuComponent:
    MENU = '.products-menu'

    def __init__(self, page):
        self.page = page

    @property
    def menu(self):
        return self.page.locator(self.MENU)

    def get_category(self, text):
        return self.menu.get_by_text(text.strip(), exact=True)

    def get_subcategory(self, text):
        return self.menu.get_by_text(text.strip(), exact=True)

    def open_subcategory(self, category_text, subcategory_text):
        category = self.get_category(category_text)
        category.hover()
        submenu = self.get_subcategory(subcategory_text)
        submenu.click()




