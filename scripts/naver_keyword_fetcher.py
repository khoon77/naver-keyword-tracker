import requests
import os
from datetime import datetime

# ✅ GitHub Secrets에서 가져온 환경 변수 (GitHub Actions 실행 시 자동 연결)
client_id = os.getenv('NAVER_CLIENT_ID')
client_secret = os.getenv('NAVER_CLIENT_SECRET')

# ✅ 인기 키워드 목록 (원하면 구글 트렌드, 네이버 트렌드에서 자동으로 가져올 수 있음)
keywords = ['장마', '폭염', '여름휴가', '태풍', '냉방병']

# ✅ 네이버 블로그 검색 API 호출
def search_blog(keyword):
    url = "https://openapi.naver.com/v1/search/blog.json"
    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret
    }
    params = {
        "query": keyword,
        "display": 1,  # 가장 최신 1개만 가져오기
        "sort": "date"
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

# ✅ 전체 흐름 제어
def main():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open("log.txt", "a", encoding='utf-8') as f:
        f.write(f"\n[{now}] 네이버 인기 키워드 블로그 검색 결과\n")
        for kw in keywords:
            result = search_blog(kw)
            item = result.get("items", [{}])[0]
            title = item.get("title", "(검색 결과 없음)")
            link = item.get("link", "")
            f.write(f" - {kw}: {title} / {link}\n")

if __name__ == "__main__":
    main()


