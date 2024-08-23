from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)

def wait_until(xpath):
    WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))


browser.get('http://www.naver.com/')
# e = browser.find_element(By.ID, 'query')
# e.send_keys('여행으로 이동할게욤;')
# time.sleep(2)
# e.send_keys(Keys.ENTER)
browser.maximize_window()
time.sleep(2)
url = "https://flight.naver.com/"
browser.get(url)
#1. 가는 날 선택
e = browser.find_element(By.XPATH, '//button[text()="가는 날"]')
e.click()
time.sleep(1)
#이번달(28) 클릭
xpath = '//b[text()="28"]'
wait_until(xpath)
es = browser.find_elements(By.XPATH, xpath)
es[0].click()

xpath = '//b[text()="30"]'
wait_until(xpath)
es = browser.find_elements(By.XPATH, xpath)
es[0].click()

# #2. 이번달 28일, 26일 선택
# es = browser.find_elements(By.XPATH, '//b[text()="28"]')
# es[0].click()
# time.sleep(1)
# es = browser.find_elements(By.XPATH, '//b[text()="30"]')
# es[0].click()
# time.sleep(1)
#도착지 선택
e = browser.find_element(By.XPATH, '//b[text()="도착"]')
e.click()
time.sleep(1)
#국내 선택
e = browser.find_element(By.XPATH, '//button[text()="일본"]')
e.click()
time.sleep(1)
#제주국제공항 선택
e = browser.find_element(By.XPATH, '//i[contains(text(), "도쿄")]')
e.click()
#항공권 검색 버튼 선택
e = browser.find_element(By.XPATH, '//span[contains(text(), "검색")]')
e.click()   
#첫 번째 결과를 출력할 때까지 최대 10초 기다린다.
# first = '//*[@id="__next"]/div/main/div[4]/div/div[2]/div[2]'
# first = '//*[@id="container"]/div[5]/div/div[3]/div[1]/div/div[1]/div'
# WebDriverWait(browser, 20).until(EC.presence_of_all_elements_located((By.XPATH, first)))
# #첫 번째 결과 출력
# e = browser.find_element(By.XPATH, first)
# print(e.text)
first = '//*[@id="container"]/div[4]/div/div[4]/div[1]/div/div[1]'
wait_until(first)
e = browser.find_element(By.XPATH, first)
# print(e.text)

# 검색목록
es = browser.find_elements(By.XPATH, '//*[contains(@class, "concurrent_ConcurrentItemContainer__NDJda")]')
es = es[:10]
for e in es:
    print(e.text)
    print('-' * 80)
print("전체 검색 수 : ", len(es))

