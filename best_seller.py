import requests
from bs4 import BeautifulSoup

# 교보문고 베스트셀러 페이지 URL
url = "https://www.kyobobook.co.kr/bestSellerNew/bestseller.laf"

# 웹 페이지 요청
response = requests.get(url)

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(response.text, "html.parser")

# 책 제목을 가져오는 CSS 선택자
titles = soup.select(".title")

# 상위 10개 책 제목 출력
for idx, title in enumerate(titles[:10], start=1):
    print(f"{idx}위: {title.get_text().strip()}")
