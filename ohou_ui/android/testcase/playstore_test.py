import os
import traceback
from selenium.common.exceptions import NoSuchElementException


from ohou_ui.android.pages.playstore_page import *
from ohou_ui.android.utils.set_clipboard import set_clipboard


class PlayStoreTestCase:

    def search_and_open_app(self, wd):
        try:
            playstore = PlayStore(wd)
            # 플레이스토어 검색 버튼 클릭
            search_btn = playstore.search_btn()
            search_btn.click()
            # 검색 필드 클릭
            search_field = playstore.search_field()
            search_field.click()
            # 검색어 입력 및 검색
            set_clipboard(wd, "오늘의집")
            # 오늘의집 앱 상세 진입
            app_name = playstore.app_name()
            app_name.click()
            # 열기 버튼 클릭, 업데이트 있다면 수행
            try:
                open_app_btn = playstore.open_app_btn()
                open_app_btn.click()
            except NoSuchElementException:
                # 업데이트 버튼 클릭 후, 열기 버튼 클릭
                try:
                    update_app_btn = playstore.update_app_btn()
                    update_app_btn.click()
                    open_app_btn.is_displayed()
                    open_app_btn.click()
                except NoSuchElementException:
                    print("No such element: 열기 버튼 or 업데이트 버튼")
                    traceback.print_exc()

        except Exception as e:
            print("스토어에서 App 검색 및 열기 테스트 실패")
            print(e)
            traceback.print_exc()




