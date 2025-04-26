from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from ohou_ui.android.utils.locators import *
from selenium.webdriver.support import expected_conditions as ec

class LogInPage:

    def __init__(self, wd):
        self.wd = WebDriverWait(wd, 10)

    def login_to_email(self):
        try:
            login_to_email_btn = self.wd.until(ec.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@resource-id='net.bucketplace:id/emailLogInText']")))
            return login_to_email_btn
        except Exception as e:
            result = "fail"
            print(e)


    def email_input(self):
        try:
            email_input = xq_hint_text(self.wd, "이메일")
            return email_input
        except Exception as e:
            result = "fail"
            print(e)


    def password_input(self):
        try:
            password_input = xq_uiauto_text(self.wd, "비밀번호")
            return password_input
        except Exception as e:
            result = "fail"
            print(e)


    def login_btn(self):
        try:
            login_btn = xq_id(self.wd, "net.bucketplace:id/loginButton")
            return login_btn
        except Exception as e:
            result = "fail"
            print(e)