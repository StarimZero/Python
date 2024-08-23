import requests 
from bs4 import BeautifulSoup


url = 'http://www.cgv.co.kr/movies/'
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

print(soup.title)
print(soup.title.get_text())




#'div' 태그이면서 class 이름이 'sec-movie-chart' 검색
movie = soup.find('div', attrs={'class':'sect-movie-chart'})
movies = movie.find_all('li')
#print(len(movies))
for index, m in enumerate(movies):
    title = m.find('strong', attrs={'class', 'title'}).get_text()
    img = m.find('img').attrs['src']
    link = m.find('a', attrs={'class', 'link-reservation'})['href']
    date = m.find('span', attrs={'class', 'txt-info'}).find('strong').get_text().strip()
    percent = m.find('strong', attrs={'class', 'percent'}).find('span').get_text()
    print(str(index+1), title)
    print(img)
    print('http://www.cgv.co.kr' + link)
    print('개봉일:', date[0:10])
    print('예매율 : ', percent)
    print('-' * 80)

    