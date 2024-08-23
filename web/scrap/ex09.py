import requests
from bs4 import BeautifulSoup
import re

query = '장원영'
url ='https://www.google.com/search?q={}&sca_esv=0938baf10882972d&sca_upv=1&udm=2&biw=1920&bih=939&ei=vsSyZqTIKqzd1e8P2qXN4Qk&ved=0ahUKEwikn9vU1OGHAxWsbvUHHdpSM5wQ4dUDCBE&uact=5&oq=%EC%9E%A5%EC%9B%90%EC%98%81&gs_lp=Egxnd3Mtd2l6LXNlcnAiCeyepeybkOyYgTILEAAYgAQYsQMYgwEyBRAAGIAEMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyBRAAGIAEMg4QABiABBixAxiDARiKBTIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgARIlApQ2QFY6wlwBHgAkAEAmAFroAH4BqoBAzQuNbgBA8gBAPgBAZgCBqACvwKoAgDCAggQABiABBixA5gDAYgGAZIHAzQuMqAHtCs&sclient=gws-wiz-serp'.format(query)
headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Whale/3.27.254.15 Safari/537.36",
        "Accept-Language":"ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"
    }
res = requests.get(url, headers=headers) #문서가져오기
soup = BeautifulSoup(res.text, 'lxml') #xml로 파싱하기

#print(res.text)
with open('data/image.html', 'w', encoding='utf-8') as file: #파일로 쓰기 
    file.write(soup.prettify())

es = soup.find_all('div', attrs={'class':re.compile('^eA0Zlc')})

print(len(es))
for index, e in enumerate(es):
    title = e.find('div', attrs={'class' : 'toI8Rb OSrXXb'})
    print(index+1, title.get_text())
