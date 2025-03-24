import requests
from bs4 import BeautifulSoup

# 왓챠 인기 콘텐츠 페이지 URL
url = "https://watcha.com/contents/rank"

# 웹 페이지 요청
response = requests.get(url)

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(response.text, "html.parser")

# 콘텐츠 제목을 가져오는 CSS 선택자
titles = soup.select(".css-1okxopb")[:10]  # 상위 10개 콘텐츠만 가져오기

# 인기 콘텐츠 출력
print("=== 왓챠 인기 콘텐츠 TOP 10 ===")
for idx, title in enumerate(titles, start=1):
    print(f"{idx}위: {title.text.strip()}")
