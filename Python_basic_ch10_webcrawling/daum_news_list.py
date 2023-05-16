import requests
from bs4 import BeautifulSoup
from daum_news_fnc import get_news_title_and_content

url = "https://v.daum.net/v/20230509090530015"

result = requests.get(url)
soup = BeautifulSoup(result.text,"html.parser")
title_list = soup.select("ul.list_news2a.link_txt")
for i, tag in enumerate(title_list):
    new_url = tag["href"]
    title, content = get_news_title_and_content(new_url)
    print("=" * 100)
    print(f"{i+1} 뉴스 제목: {title}")
    print("=" * 100)