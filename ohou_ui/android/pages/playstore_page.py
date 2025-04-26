from selenium.webdriver.support.ui import WebDriverWait
from ohou_ui.android.utils.locators import *

class PlayStore:

    def __init__(self, wd):
        self.wd = WebDriverWait(wd, 10)

    def search_btn(self):
        try:
            search_btn = xq_text(self.wd, "검색")
            return search_btn

        except Exception as e:
            result = "fail"
            print(e)

    def search_field(self):
        try:
            search_field = xq_text(self.wd, "앱 및 게임 검색")
            return search_field
        except Exception as e:
            result = "fail"
            print(e)

    def app_name(self):
        try:
            app_name = xq_access(self.wd, "오늘의집 - 라이프스타일 슈퍼앱\n설치됨\n")
            return app_name
        except Exception as e:
            result = "fail"
            print(e)


    def open_app_btn(self):
        try:
            open_app_btn = xq_access(self.wd, "열기")
            return open_app_btn
        except Exception as e:
            result = "fail"
            print(e)

    def update_app_btn(self):
        try:
            update_app_btn = xq_access(self.wd, "업데이트")
            return update_app_btn
        except Exception as e:
            result = "fail"
            print(e)
