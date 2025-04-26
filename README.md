# ohou_automation

## 프로젝트 구조
~~~
ohou_automation

├── ohou_ui     # UI 테스트 자동화 
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
└── rest_api    # API 테스트 자동화
│  ├── SKT_openai   # SKT rest api 테스트
│      └── testcase.py  # 테스트 코드
└── __init__.py
~~~

<br/>

## UI 테스트 자동화 
### ⚫ 테스트 환경
- Python 3.11.4
- Python unittest
- Appium 2.12.0
- Android 실물 기기
- InteliJ Idea
- POM 구조
- 테스트 종료 시 /Reports 폴더에 테스트 결과 리포트 저장(HTML)

### 🟡 테스트 케이스
- 앱 설치 테스트
  - TC1. 플레이스토어 검색 버튼 클릭
  - TC2. 검색 필드 클릭
  - TC3. 검색어 입력 및 검색
  - TC4. 오늘의집 앱 상세 진입
  - TC5. 앱 설치
- 앱 실행 테스트
  - TC6. 로그인 버튼 클릭(이메일 로그인)
  - TC7. 이메일 입력 필드에 이메일 입력
  - TC8. 비밀번호 입력 필드에 비밀번호 입력
  - TC9. 로그인 버튼 클릭
  - TC10. 메인 진입 확인 (필요 시, 관심사 페이지 스킵 가능)

### 🟢 테스트 실행 방법 (Appium)
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

<br/>

## API 테스트 자동화
### ⚫ 테스트 환경
- Python 3.11.4

### 🟡 테스트 케이스
- 테스트 흐름
  - TC1. 장소 검색
    - 응답코드 200, 인자로 전달한 키워드가 검색 결과에 포함되었는지 확인, 검색 결과 정합석 확인
  - TC2. 장소 상세 조회
    - 응답코드 200, TestData - 위도/경도 값 추출
  - TC3. 주소 → 좌표 변환
    - 응답코드 200, 반환 주소 문자열 확인 
  - TC4. 좌표 → 주소 변환
    - 응댭코드 200, TestData인 좌표값을 통한 주소 바인딩. TestData 정합성 검증
  - TC5. 보행 경로 탐색 후, 예상 거리와 시간 반환

### 🟢 테스트 실행 방법
 #### 1. 해당 Repo를 클론한 후, pip install -r requirements.txt로 라이브러리를 설치합니다. 
 #### 2. rest_api/SKT_openapi/testcase.py 코드를 확인합니다.
 #### 3. 코드 최상단 HEADERS 배열의 appKey값을 본인 값으로 변경합니다.
    appKey는 https://openapi.sk.com/products/detail?svcSeq=60&menuSeq=122 를 참고하여 발급받을 수 있습니다.
 #### 4. python testcase.py 로 실행합니다. 
~~~
//예상 출력값

[search_place] 검색 결과 5개
[get_place_detail] 상세 조회 성공: None
[geocode_address] 변환된 좌표: (37.567101, 126.976983)
[reverse_geocode] 변환된 주소: 서울특별시 중구 명동,서울특별시 중구 태평로1가 60-20,서울특별시 중구 세종대로 119
[find_route] 예상 거리: 128m, 예상 시간: 106s
