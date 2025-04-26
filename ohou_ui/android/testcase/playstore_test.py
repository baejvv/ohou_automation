import os
import traceback
from time import sleep, time
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from ohou_ui.android.pages.playstore_page import *
from ohou_ui.android.utils.set_clipboard import set_clipboard


class PlayStoreTestCase:

    def search_and_open_app(self, wd):
        try:
            wd.remove_app("net.bucketplace")

            playstore = PlayStorePage(wd)
            # TC1. 플레이스토어 검색 버튼 클릭
            search_btn = playstore.search_btn()
            search_btn.click()
            # TC2. 검색 필드 클릭
            search_field = playstore.search_field()
            search_field.click()
            # TC3. 검색어 입력 및 검색
            set_clipboard(wd, "오늘의집")
            # TC4. 오늘의집 앱 상세 진입
            app_name = playstore.app_name()
            app_name.click()
            # TC5. 앱 설치
            install_app_btn = playstore.install_app_btn()
            install_app_btn.click()

            start = time()
            wait_limit_seconds = 60
            while True:
                now = time()
                if now - start > wait_limit_seconds:
                    print(f'앱 설치{int(now - start)}sec 경과, 엘리먼트 찾기 실패')
                    raise Exception
                try:
                    open_app_btn = playstore.open_app_btn()
                    open_app_btn.is_displayed()
                    break
                except NoSuchElementException or TimeoutException:
                    pass

            #TODO. 테스트 시작부터 제거 후 설치가 아니라면 고려해볼만한 옵션
            '''
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
            '''


        except Exception as e:
            print(e)
            traceback.print_exc()
            # 여기서 에러났다면 앱 제거
            try:
                wd.remove_app("net.bucketplace")
            except Exception:
                pass




