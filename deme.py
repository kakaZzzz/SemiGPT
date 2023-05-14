import requests
import json
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250'
movies = []

for start in range(0, 250, 25):
    response = requests.get(url, params={'start': start})
    soup = BeautifulSoup(response.text, 'html.parser')
    for item in soup.select('.item'):
        title = item.select_one('.title').text.strip()
        rating = item.select_one('.rating_num').text.strip()
        year = item.select_one('.year').text.strip('()')
        movies.append({'title': title, 'rating': rating, 'year': year})

with open('douban_top250.json', 'w', encoding='utf-8') as f:
    json.dump(movies, f, ensure_ascii=False, indent=2)