import requests 
from bs4 import BeautifulSoup
import re, csv

url = 'https://finance.naver.com/sise/sise_quant.naver'
headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Whale/3.27.254.15 Safari/537.36",
        "Accept-Language":"ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"
    }
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')
es = soup.find('table', attrs={'class':'type_2'}).find_all('tr')

file = open('data/코스피거래상위 1위부터 100위까지.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(file)
title = 'N	종목명	현재가	전일비	등락률	거래량	거래대금	매수호가	매도호가	시가총액	PER	ROE'.split('\t')
writer.writerow(title)

for e in es:
    columns = e.find_all('td')
    if len(columns) <= 1:
        continue
    data = []
    for col in columns:
        # col = col.get_text()
        # col = re.sub('\n|\t|상승|하락|보합', '', col)
        # data.append(col)
        # data.append(col.get_text().split())
        # data = [column.get_text().strip() for column in columns]
        data = [re.sub('\n|\t|상승|하락|보합', '', col.get_text()) for col in columns]
    writer.writerow(data)
    print(data)
    

