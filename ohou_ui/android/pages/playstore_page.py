from selenium.webdriver.support.ui import WebDriverWait
from ohou_ui.android.utils.locators import *

class PlayStore:

    def __init__(self, wd):
        self.wd = WebDriverWait(wd, 10)

    def search_btn(self):

        try:
            search_btn = xq_text_text(self.wd, "검색")
            return search_btn

        except Exception as e:
            result = "fail"
            msg = f'플레이스토어 진입 실패: {e}'
            print(e)