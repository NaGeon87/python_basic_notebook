import requests
from bs4 import BeautifulSoup
from daum_news_fnc import get_news_title_and_content
page = 3  # 수집 할 페이지수
cnt = 0  # 수집 기사수를 저장하는 변수
for page_num in range(1, page+1):
    print(f"{page_num} page ==========================================")
    url = f"https://news.daum.net/breakingnews/digital?page={page_num}"

    result = requests.get(url)
    soup = BeautifulSoup(result.text,"html.parser")
    title_list = soup.select("ul.list_news2 a.link_txt")

    for i, tag in enumerate(title_list):
        new_url = tag["href"]
        title, content = get_news_title_and_content(new_url)
        cnt += 1
        print("=" * 100)
        print(f"URL: {new_url}")
        print(f"{cnt}")
        print(f"{i+1} 뉴스 제목: {title}")
        print("=" * 100)