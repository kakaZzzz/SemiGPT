import json
import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
movies = []
for movie in soup.find_all('div', class_='info'):
    title = movie.find('span', class_='title').text
    score = movie.find('span', class_='rating_num').text
    author = movie.find('p', class_='').text.strip().split('\n')[0]

    movies.append({
        'title': title,
        'score': score,
        'author': author
    })

with open('douban_top250.json', 'w', encoding='utf-8') as f: 
    json.dump(movies, f, indent=4, ensure_ascii=False)