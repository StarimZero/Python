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

    url ='https://land.naver.com/'
    browser.get(url)

    e = browser.find_element(By.ID, 'queryInputHeader')
    e.send_keys('송도더샵')
    e.send_keys(Keys.ENTER)

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(browser.page_source, "lxml")

    es = soup.find_all("a", attrs={"class":"item_link"})
    for e in es:
        title = e.find("div", attrs={"class":"title"})
        address = e.find("div", attrs={"class":"address"})
        type = e.find("strong", attrs={"class":"type"})
        info = e.find("div", attrs={"class":"info_area"})
        specs = info.find_all("span", attrs={"class":"spec"})
        print("이름 : " + title.get_text(), "주소 : " + address.get_text(), "타입 : " + type.get_text())
        print("\n-----------------------------------------------")
        for spec in specs:
            print(spec.get_text() + "|", end="")
            print("\n-----------------------------------------------")
        

browser_execute()