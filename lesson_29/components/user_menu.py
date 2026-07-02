class UserMenuComponent:

    DROPDOWN_MENU = ".userbar__menu"
    USER_ICON = ".userbar__button-icon-initials"

    def __init__(self, page):
        self.page = page

    @property
    def user_icon(self):
        return self.page.locator(self.USER_ICON)

    @property
    def dropdown(self):
        return self.page.locator(self.DROPDOWN_MENU)

    def open(self):
        self.user_icon.hover()
        self.dropdown.wait_for(state="visible")
