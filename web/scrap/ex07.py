import requests 
from bs4 import BeautifulSoup
import re, csv

def create_soup(page):
    url = 'https://finance.naver.com/sise/sise_market_sum.naver?&page={}'.format(page)
    headers = {
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Whale/3.27.254.15 Safari/537.36",
            "Accept-Language":"ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"
        }
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    return soup


file = open('data/코스피시총상위 1위부터 100위까지.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(file)
title = 'N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE'.split('\t')
writer.writerow(title)

for i in range(1,3):
    soup = create_soup(i)
    es = soup.find('table', attrs={'class':'type_2'}).find_all('tr')


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
        
    

