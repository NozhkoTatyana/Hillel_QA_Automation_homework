from playwright.sync_api import Page
from lesson_29.components.user_menu import UserMenuComponent


class LoginPage:

    EMAIL_FIELD = "#login-form-email"
    PASSWORD_FIELD = "#login-form-password"
    LOGIN_BUTTON_FORM = "//span[text()='Увійти']"
    SIGN_IN_BUTTON = "a[data-modal='#sign-in']"
    AGE_CONFIRM_BUTTON = "button:has-text('Так, мені виповнилося 18 років')"


    def __init__(self, page: Page):
        self.page = page

    @property
    def email_field(self):
        return self.page.locator(self.EMAIL_FIELD)

    @property
    def password_field(self):
        return self.page.locator(self.PASSWORD_FIELD)

    @property
    def login_button_form(self):
        return self.page.locator(self.LOGIN_BUTTON_FORM)

    @property
    def sign_in_button(self):
        return self.page.locator(self.SIGN_IN_BUTTON).first

    @property
    def age_confirm_button(self):
        return self.page.locator(self.AGE_CONFIRM_BUTTON)

    def open(self):
        self.page.goto("https://shos.com.ua/")

    def confirm_age(self):
        self.age_confirm_button.click()

    def click_login_button_form(self):
        self.login_button_form.click()

    def fill_form_auth(self, email: str, password: str):
        self.email_field.fill(email)
        self.password_field.fill(password)
        self.click_login_button_form()

    def authorize(self, email, password):
        user_menu = UserMenuComponent(self.page)
        self.open()
        self.confirm_age()
        self.sign_in_button.click()
        self.fill_form_auth(email, password)
        user_menu.user_icon.wait_for(state="attached")
