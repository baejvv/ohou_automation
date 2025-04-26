import os
import requests
import unittest


API_KEY = os.getenv("SK_OPENAPI_KEY")
BASE_URL = "https://apis.openapi.sk.com"
HEADERS = {
    "accept": "application/json",
    "appKey": "kgZ9b3zTizamnilzmy0Yi7ujm95nYuJK4GpxpzAa"
}

# TC 1. 응답코드 200, 인자로 전달한 키워드가 검색 결과에 포함됐느닞 확인, 검색 결과 5개 확인
# 장소 ID/위경도 추출
def search_place(keyword):
    url = f"{BASE_URL}/tmap/pois"
    params = {
        "version": 1,
        "searchKeyword": keyword,
        "resCoordType": "WGS84GEO",
        "reqCoordType": "WGS84GEO",
        "count": 5,
        "centerLat": 37.5665,  # 서울 중심 좌표
        "centerLon": 126.9780
    }
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status() # 응답 코드 검증

    data = response.json()
    pois = data.get("searchPoiInfo", {}).get("pois", {}).get("poi", [])

    if not pois:
        raise Exception(f"키워드인 스타벅스를 찾지 못했습니다.: {keyword}")

    print(f"[search_place] 검색 결과 {len(pois)}개")
    if len(pois) != 5:
        raise Exception("응답값의 검색 결과 갯수가 요청과 다릅니다.")

    first_poi = pois[0]
    return first_poi["id"], first_poi["frontLat"], first_poi["frontLon"]

# TC 2. 응답코드 200, TestData - 위도/경도 값 추출 (lat=37.567101, lon=126.976983)
def get_place_detail(poi_id):
    url = f"{BASE_URL}/tmap/pois/{poi_id}"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    data = response.json()

    print(f"[get_place_detail] 상세 조회 성공: {data.get('name')}")
    return data

# TC 3. 응답코드 200, 반환 주소 문자열에 "시 : 서울특별시 / 구 : 중구 / 동 : 명동 포함 확인
# 지오코딩 즉, TC 3의 TestData인 위/경도를 기반으로 좌표값 TestData로 저장
def geocode_address(city_do, gu_gun, dong):
    """ 주소 → 좌표 변환 (Geocoding) """
    url = f"{BASE_URL}/tmap/geo/geocoding"
    params = {
        "version": 1,
        "city_do": city_do,
        "gu_gun": gu_gun,
        "dong": dong,
        "coordType": "WGS84GEO"
    }
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    data = response.json()

    coordinate_info = data.get("coordinateInfo", {})

    if not coordinate_info:
        raise Exception(f"지오코딩 실패, ({city_do}, {gu_gun}, {dong})")

    lat = coordinate_info.get("lat")
    lon = coordinate_info.get("lon")

    if not lat or not lon: # 좌표값 비어있으면 Exception
        raise Exception(f"응답값에 좌표값이 없습니다. {city_do}, {gu_gun}, {dong}")
    print(f"[geocode_address] 변환된 좌표: ({lat}, {lon})")

    return lat, lon

# TC 4. 응댭코드 200, TestData인 좌표값을 통한 주소를 얻는다.
# TestData의 정합성을 검증할 수 있음.
def reverse_geocode(lat, lon):
    url = f"{BASE_URL}/tmap/geo/reversegeocoding"
    params = {
        "version": 1,
        "lat": lat,
        "lon": lon,
        "coordType": "WGS84GEO",
        "addressType": "A10"
    }
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()

    data = response.json()
    address = data.get("addressInfo", {}).get("fullAddress")

    if not address:
        raise Exception(f"Reverse geocoding failed for coordinates: ({lat}, {lon})")
    print(f"[reverse_geocode] 변환된 주소: {address}")

    return address

# TC 5. 보행자 경로 안내
# TODO. 주석 코드는 응답코드 200, 거리 128m, 시간 106초 가 나와야 하며, 실시간 반영이기 때문에 테스트 목적에 따라 TC를 변경 후 그에 맞게 거리와 시간 조절이 필요함.
def find_route(start_lat, start_lon, end_lat, end_lon):
    """ 경로 탐색 (Single Route) """
    url = f"{BASE_URL}/tmap/routes/pedestrian"
    params = {
        "version": 1,
        "startX": start_lon,
        "startY": start_lat,
        "endX": end_lon,
        "endY": end_lat,
        "startName": "출발지",
        "endName": "도착지",
        "reqCoordType": "WGS84GEO",
        "resCoordType": "WGS84GEO"
    }
    response = requests.post(url, headers=HEADERS, params=params)
    response.raise_for_status()

    data = response.json()
    summary = data.get("features", [])[0].get("properties", {})

    # if summary.get('totalDistance', 'Unknown') != 128:
    #     raise Exception('응답값의 예상 거리가 128m와 다릅니다.',  f"실제 결과: {summary.get('totalDistance', 'Unknown')}m")
    #
    # if summary.get('totalTime', 'Unknown') != 106:
    #     raise Exception('응답값의 예상 소요 시간이 106s와 다릅니다.',  f"실제 결과: {summary.get('totalTime', 'Unknown')}m")

    print(f"[find_route] 예상 거리: {summary.get('totalDistance', 'Unknown')}m, 예상 시간: {summary.get('totalTime', 'Unknown')}s")
    return summary


def run_test_flow():
    """ 전체 테스트 플로우 실행 """
    # 1. 장소 검색
    poi_id, poi_lat, poi_lon = search_place("스타벅스")

    # 2. 장소 상세 조회
    get_place_detail(poi_id)

    # 3. 주소 → 좌표 변환
    city_do = "서울특별시"
    gu_gun = "중구"
    dong = "태평로1가"
    lat, lon = geocode_address(city_do, gu_gun, dong)

    # 4. 좌표 → 주소 변환
    reverse_geocode(lat, lon)

    # 5. 보행 경로 탐색 후, 예상 거리와 시간 반환
    find_route(start_lat=lat, start_lon=lon, end_lat=poi_lat, end_lon=poi_lon)


if __name__ == "__main__":
    run_test_flow()