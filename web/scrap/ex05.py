import requests 
from bs4 import BeautifulSoup
import re

def create_soup(query, page):
    url = 'https://www.coupang.com/np/search?rocketAll=true&searchId=f1ef429458ed44f0aa26f5b18db1a711&q={}\
            &brand=&offerCondition=&filter=&availableDeliveryFilter=&filterType=rocket_luxury%2Crocket_wow%2Ccoupang_global&isPriceRange=false&priceRange=&minPrice=&maxPrice=\
            &page={}&trcid=&traid=&filterSetByUser=true&channel=user&backgroundColor=&searchProductCount=360&component=&rating=0&sorter=scoreDesc&listSize=36'.format(query, page)
    headers = {
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Whale/3.27.254.15 Safari/537.36",
            "Accept-Language":"ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"
        }
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    return soup
index = 0
items = []
for i in range(1, 2):
    soup = create_soup('뜨개', i)
    es = soup.find_all("li", attrs={"class":re.compile("^search-product")})
    for e in es:
        name = e.find('div', attrs={'class':'name'})
        if name:
            name = name.get_text().strip()
        else:
            continue
        price = e.find('strong', attrs={'class':'price-value'})
        if price:
            price = price.get_text().strip()
        else:
            continue
        image = e.find('img', attrs={'class':'search-product-wrap-img'})
        if image:
            image = 'https:' + image['src']
        else:
            continue
        index += 1
        print(index, "상품명 : " + name, "가격 : " + price, "이미지보기 : " + image)
        print("-" * 150)

        item = {'name':name, 'price':price, 'image':image}
        items.append(item)

#items를 JSON파일로 저장
import json
with open('data/shop.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(items, indent=4, sort_keys=True, ensure_ascii=False))


        #이미지 다운로드
        # res_image = requests.get(image)
        # with open('images/img{}.jpg'.format(index), 'wb') as file:
        #     file.write(res_image.content)

