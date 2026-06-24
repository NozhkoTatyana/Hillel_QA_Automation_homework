from lesson_29.components.menu_component import MenuComponent

class HomePage:

    def __init__(self, page):
        self.page = page
        self.menu = MenuComponent(page)

    def open(self):
        self.page.goto("https://shos.com.ua")