import os
import traceback
import logging
from time import sleep
from selenium.common.exceptions import NoSuchElementException


from ohou_ui.android.pages.login_page import *
from ohou_ui.android.pages.main_page import *
from ohou_ui.android.utils.set_clipboard import set_clipboard


class LogInTestCase:

    def login(self, wd):
        try:
            login = LogInPage(wd)
            # TC6. 이메일로 로그인 버튼 선택
            login_btn = login.login_to_email()
            login_btn.click()

            email = os.environ.get("EMAIL")
            password = os.environ.get("PASSWORD")
            # TC7. 이메일 입력 필드에 이메일 입력
            email_input_field = login.email_input()
            email_input_field.clear()
            email_input_field.send_keys(email)
            # TC8. 비밀번호 입력 필드에 비밀번호 입력
            password_input_field = login.password_input()
            password_input_field.send_keys(password)
            # TC9. 로그인 버튼 클릭
            login_btn = login.login_btn()
            login_btn.click()

            main_page = MainPage(wd)
            # 관심사 페이지 랜딩되면 back
            # try:
            #     main_page.interests_page().is_displayed()
            #     wd.back()
            # except NoSuchElementException:
            #     pass

            # TC10. 메인 진입 확인
            main_page.shopping_btn().is_displayed()


        except Exception as e:
            traceback.print_exc()
            logging.error(e)

