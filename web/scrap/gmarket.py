from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def browser_execute():
    options = webdriver.ChromeOptions()
    #options.add_argument("headless")
    options.add_argument('user-argument=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Whale/3.27.254.15 Safari/537.36')
    options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()

    url ='https://www.gmarket.co.kr/'
    browser.get(url)

    e = browser.find_element(By.ID, 'form__search-keyword')
    e.send_keys('노트북')
    e.send_keys(Keys.ENTER)
    interval = 2
    prev_height = browser.execute_script("return document.body.scrollHeight")
    #browser.execute_script('alert(document.body.scrollHeight)')

    #페이지의 마지막까지 스크롤 내리기
    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(interval)
        curr_height = browser.execute_script("return document.body.scrollHeight")
        if prev_height == curr_height:
            break
        else:
            prev_height = curr_height
    print("스크롤 완료")

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(browser.page_source, "lxml")

    es = soup.find_all("div", attrs={"class":"box__item-container"})
    print(len(es))
    for e in es:
        title = e.find("span", attrs={"class":"text__item"})
        sale = e.find("span", attrs={"class" : "text text__value"})
        if sale:
            sale = e.get_text()
        else:
            sale =""
        price = e.find("strong", attrs={'class': "text text__value"})
        image = 'http:' + e.find('img')['src']
        print("이름 : " + title.get_text(), "할인율 : " + sale, "가격 : " + price.get_text(), "이미지 : " + image)
        print("\n-----------------------------------------------")

        

browser_execute()