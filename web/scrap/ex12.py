import requests, re
from bs4 import BeautifulSoup



def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    return soup

def weather():
    url ='https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EB%8C%80%EA%B5%AC%EB%82%A0%EC%94%A8&oquery=%EC%98%A4%EB%8A%98%EC%9D%98+%EB%82%A0%EC%94%A8&tqi=irKSQspzLiwssnQX0QVssssstYl-443500'
    soup = create_soup(url)
    temp = soup.find('div', attrs={'class':'temperature_text'})
    temp = re.sub('현재 온도', '', temp.get_text())
    print(temp)


def news():
    url = 'https://news.naver.com/section/104'
    soup = create_soup(url)
    es = soup.find('ul', attrs={'class':'sa_list'}).find_all('li', limit=5)
    items=[]
    for e in es:
        title = e.find('strong', attrs={'class':'sa_text_strong'}).get_text()
        link = e.find('a')['href']
        print(title, link)
        data = {'title':title, 'link':link}
        items.append(data)
    return items


def english():
    url = 'https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=...&logger_kw=...'
    soup = create_soup(url)
    es = soup.find_all('div', attrs={'id':re.compile('^conv_kor_t')})
    korean = []
    for e in es[:4]:
        print(e.get_text().strip())
        data = {'sentence':e.get_text().strip()}
        korean.append(data)
    english = []
    for e in es[4:8]:
        print(e.get_text().strip())
        data = {'sentence':e.get_text().strip()}
        english.append(data)
    return {'korean':korean, 'english':english}


print(english(), news(), weather())

    







