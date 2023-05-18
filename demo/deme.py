from selenium import webdriver
import json

url = 'https://movie.douban.com/top250'
driver = webdriver.Chrome()
driver.get(url)

movies = []
for i in range(10):  # 抓取前10页,每页25条信息
    driver.find_element_by_class_name('next').click()
    li_list = driver.find_elements_by_tag_name('li')
    for li in li_list:
        movie = {}
        movie['ranking'] = li.find_element_by_class_name('pic').find_element_by_tag_name('em').text
        movie['name'] = li.find_element_by_class_name('info').find_element_by_tag_name('a').text
        movie['score'] = li.find_element_by_class_name('star').find_element_by_tag_name('span').text
        movie['quote'] = li.find_element_by_class_name('quote').find_element_by_tag_name('span').text
        movies.append(movie)

with open('douban_top250.json', 'w', encoding='utf-8') as f:
    json.dump(movies, f, ensure_ascii=False, indent=4)

driver.close()