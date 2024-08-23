import requests 
from bs4 import BeautifulSoup


url = 'https://finance.naver.com/'
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')


e = soup.find('div', attrs={'class' : 'aside_area aside_popular'}).find('tbody')
es = e.find_all('tr')
for index, e in enumerate(es):
    title = e.find('a').get_text()
    td = e.find_all('td')
    price = td[0].get_text()
    updown = td[1].find('span').get_text().strip()
    updownPrice = td[1].find('span', attrs={'class' : 'tah p11 nv01'}).get_text().strip()
    
    print(str(index+1), title, price, updown, updownPrice)
