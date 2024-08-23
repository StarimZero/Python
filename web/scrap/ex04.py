import requests 
from bs4 import BeautifulSoup
import re


for i in range (1,5):
    print("현재페이지", i)
    url = 'https://www.coupang.com/np/search?rocketAll=true&searchId=4484c966375b47c9a1d2f365d582056c&q=%EB%85%B8%ED%8A%B8%EB%B6%81&brand=&offerCondition=&filter=&availableDeliveryFilter=&filterType=rocket_luxury%2Crocket%2Ccoupang_global&isPriceRange=false&priceRange=&minPrice=&maxPrice=&page={}&trcid=&traid=&filterSetByUser=true&channel=user&backgroundColor=&searchProductCount=360&component=&rating=0&sorter=scoreDesc&listSize=36'.format(i)
    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Whale/3.27.254.15 Safari/537.36",
        "Accept-Language":"ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"
    }

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    es = soup.find_all("li", attrs={"class":re.compile("^search-product")})
    index = 0

    for e in es:
        name=e.find("div", attrs={"class": "name"}).get_text()
        #애플 제품 제외
        if 'Apple' in name:
            # print("<Apple 상품 제외합니다>")
            # print("-" * 200)
            continue
        price=e.find("strong", attrs={"class": "price-value"})
        if price :
            price = price.get_text()
        else:
            continue
        #평점
        rate = e.find("em", attrs={"class": "rating"})
        if rate:
            rate = rate.get_text()
        else:
            # print("<평점 없는 상품 제외합니다>")
            # print("-" * 100)
            continue
        #리뷰 수
        rate_cnt = e.find("span", attrs={"class": "rating-total-count"})
        if rate_cnt:
            rate_cnt = rate_cnt.get_text()
            rate_cnt = rate_cnt[1:-1]
        else:
            # print("<평점 수 없는 상품 제외합니다>")
            # print("-" * 100)
            continue
        link = e.find('a', attrs={"class":"search-product-link"})['href']
        if float(rate) >= 4.5 and int(rate_cnt) >= 1000:
            index += 1
            print(index+1, "제품명 : " + name.strip(), '가격 : '+ price, '평점 : ' + rate, "리뷰 수 : " + rate_cnt)
            print("바로가기 :  + {}".format("https://www.coupang.com" + link))
            print("-" * 200)

