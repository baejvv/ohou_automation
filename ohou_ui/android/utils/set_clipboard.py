from selenium.webdriver.support.ui import WebDriverWait

from ohou_ui.android.utils.locators import *

"""
send_keys()를 위한 EditText 계층이 없는 경우 사용
클립보드에 복사하여 붙여넣는다.
"""


def set_clipboard(wd, text):

    # 클립보드에 텍스트 복사
    wd.set_clipboard_text(f"{text}")

    #TODO. 롱프레스할 요소 찾기. 텍스트필드가 1개라는 가정이며 계층 구조에서 여러개의 EditText가 존재할 경우 보완 필요
    element = wd.find_element(AppiumBy.XPATH, '//android.widget.EditText/android.view.View')

    # lp 실행
    wd.execute_script('mobile: longClickGesture', {"elementId": element.id, 'duration': 1000})

    # "붙여넣기" 버튼 클릭
    paste_button =xq_access(WebDriverWait(wd, 10), "붙여넣기")
    paste_button.click()

    # 엔터(검색)
    wd.press_keycode(66)