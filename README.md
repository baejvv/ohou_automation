# ohou_automation

## 프로젝트 구조
~~~
ohou_automation

├── ohou_ui
│  ├── __init__.py
│  ├── __pycache__
│  └── android      # 테스트 대상 OS
│    ├── CommonConstants.py     # 공통 상수
│    ├── Reports     # 테스트 결과 리포트
│    │  ├── anyReports.html
│    ├── __init__.py
│    ├── android_setup.py   # Capability 셋업
│    ├── android_test_runner.py     # 테스트 실행
│    ├── pages  # POM 구조 - 페이지 객체
│    │  ├── __init__.py
│    │  ├── login_page.py
│    │  ├── main_page.py
│    │  └── playstore_page.py
│    ├── testcase       # POM 구조 - 테스트 케이스
│    │  ├── __init__.py
│    │  ├── login_test.py
│    │  └── playstore_test.py
│    └── utils
│      ├── __init__.py
│      ├── locators.py      # 자주 쓰는 로케이터 
│      └── set_clipboard.py     # 클립보드 복사 간소화 코드
└── rest_api
└── __init__.py
~~~

<br/>

## UI 테스트 실행 방법 (Appium)
 #### 1. 해당 Repo를 클론한 후, pip install -r requirements.txt로 라이브러리를 설치합니다. 
 #### 2. ohou_ui/android/android_setup.py.py에서 본인 단말의 정보로 변경한 후, 단말을 PC와 연결합니다.
 #### 3. ohou_ui/android/CommonConstants.py에서 본인의 계정정보로 변경합니다.
 #### 4. **루트 디렉토리 (`ohou_automation/`)** 로 이동한 후, 아래 명령어로 테스트를 실행합니다.
 #### 5. 테스트 결과는 `ohou_automation/ohou_ui/android/Reports` 폴더에 저장됩니다.

Appium서버는 러너에서 4723포트로 실행되고 종료됩니다. 테스트 시작 전 해당  포트에서 Appium서버가 실행되고 있다면 kill 후 테스트를 실행해주세요.

~~~
bash
cd /Users/{username}/IdeaProjects/ohou_automation
python -m ohou_ui.android.android_test_runner
~~~