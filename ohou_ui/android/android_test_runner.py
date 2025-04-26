import unittest
import os
import subprocess
from time import sleep
import HtmlTestRunner

from ohou_ui.android.android_setup import *
from ohou_ui.android.testcase.playstore_test import PlayStoreTestCase
from ohou_ui.android.testcase.login_test import LogInTestCase


class TestRunner(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     # Appium 서버 실행
    #     cls.server = start_appium_server()
    #     sleep(5)  # 서버 완전히 뜰 때까지 대기
    #     print("Appium 서버 실행 완료")
    #
    # @classmethod
    # def tearDownClass(cls):
    #     # Appium 서버 종료
    #     cls.server.terminate()
    #     cls.server.wait()
    #     print("Appium 서버 종료 완료")

    def setUp(self):
        self.wd_ohou = None
        self.wd_store = None

    def tearDown(self):
        if self.wd_ohou:
            self.wd_ohou.quit()
        if self.wd_store:
            self.wd_store.quit()

    def test_00_app_install_run(self):
        self.wd_store = setup_store()
        PlayStoreTestCase.search_and_open_app(self, self.wd_store)

    def test_01_login_run(self):
        self.wd_ohou = setup_ohou()
        LogInTestCase.login(self, self.wd_ohou)


# def start_appium_server():
#     # Appium 서버 실행 명령어
#     command = [
#         "appium",
#         "--allow-insecure", "chromedriver_autodownload",
#         "--port", "4723",
#     ]
#     server = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     return server


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='ohou_ui/android/Reports', combine_reports=True))
