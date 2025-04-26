from selenium.webdriver.support.ui import WebDriverWait
from ohou_ui.android.utils.locators import *

class MainPage:

    def __init__(self, wd):
        self.wd = WebDriverWait(wd, 20)

    def interests_page(self):
        try:
            interests_page = xq_uiauto_text(self.wd, "요즘 관심사는 무엇인가요?")
            return interests_page
        except Exception as e:
            result = "fail"
            print(e)


    def shopping_btn(self):
        try:
            home = xq_uiauto_text(self.wd, "쇼핑")
            return home
        except Exception as e:
            result = "fail"
            print(e)




