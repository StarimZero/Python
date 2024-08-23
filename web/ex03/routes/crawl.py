from flask import Blueprint, render_template, request
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

bp = Blueprint('crawl', __name__, url_prefix='/crawl')


def browser_config(url, query):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys

    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument('user-argument=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Whale/3.27.254.15 Safari/537.36')
    options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()

    browser.get(url)
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'queryInputHeader')))
    e = browser.find_element(By.ID, 'queryInputHeader')
    e.send_keys(query)
    e.send_keys(Keys.ENTER)

    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.item')))


    from bs4 import BeautifulSoup
    soup = BeautifulSoup(browser.page_source, "lxml")
    return soup


@bp.route('/house')
def house():
    return render_template('index.html', title='부동산검색', pageName='crawl/house.html')

@bp.route('/house.json')
def houseJson():
    args = request.args
    query = args['query']
    print("검색어 : " + query)

    url = 'https://land.naver.com/'
    soup = browser_config(url, query)
    es = soup.find_all('div', attrs={'class':'item'})
    items = []
    for e in es:
        title = e.find("div", attrs={"class": ["title", "item_title"]})
        address = e.find("div", attrs={"class":"address"})
        type = e.find("strong", attrs={"class":"type"})
        info = e.find("div", attrs={"class":"info_area"})
        #specs = info.find_all("span", attrs={"class":"spec"})
        item={'title':title.get_text(), 'address':address.get_text(), 'type':type.get_text(), 'info':info.get_text()}
        items.append(item)
    return items



from routes import ex12
import json
@bp.route('/news')
def news():
    result = json.dumps(ex12.news(), indent=4, ensure_ascii=False)
    return result

@bp.route('/weather')
def weather():
    return ex12.weather()

@bp.route('/english')
def english():
    result = json.dumps(ex12.english(), indent=4, ensure_ascii=False)
    return result
