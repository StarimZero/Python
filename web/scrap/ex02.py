import requests 
from bs4 import BeautifulSoup


url = 'https://finance.naver.com/'
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

es = soup.find('tbody', attrs={'id' : '_topItems1'}).find_all('tr', limit=10)
for index, e in enumerate(es):
    title = e.find('a').get_text()
    td = e.find_all('td')
    price = td[0].get_text()
    updown = td[1].get_text().strip()
    rate = td[2].get_text().strip()
    print(str(index+1),title, price, updown, rate)