import time
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room
from bs4 import BeautifulSoup
import requests

def create_soup(url): 
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    with open('soup.html', 'w', encoding='utf-8') as file: file.write(res.text)
    return soup



app = Flask(__name__)
app.secret_key = 'mysecret'
socketio= SocketIO(app)


@app.route('/')
def index():
    return 'ㅎㅇ'




@app.route('/chat') #접속은 http://localhost:5000/chat/room?uid=blue
def chat():
    uid = request.args['uid']
    # //아이디와 room 이름을 session에 저장한다.
    session['room'] = uid
    return render_template('chat.html', title='심심이', room='심심이와채팅')

@socketio.on('joined', namespace='/chat')
def joined(message):
    room = session['room']
    join_room(room)
    #클라이언트에 데이터를 송신하는 함수
    #첫 번째 인자("status"): 클라이언트에게 발생시킬 이벤트 명
    #두 번째 인자({"msg":...}): 클라이언트에게 전송한 데이터
    #세 번째 인자(room=room): 해당 이벤트를 송신할 대상 (room의 경우, 해당 그룹에 있는 세션 전체)
    emit('status', {'msg': room + '님 입장하셨습니다.'}, room=room)

@socketio.on('text', namespace='/chat')
def text(message):
    room = session.get('room')
    emit('message', {'msg':session.get('uid') + " : " + message['msg']}, room=room)
    answer_text = answer(message['msg'])
    emit('message', {'msg': '심심이' + ":" + answer_text}, room=room)

def answer(input_text): 
    answer_text = '' 
    if '안녕' in input_text: 
        answer_text = '반갑습니다.'
    elif '날씨' in input_text: 
        temp = weather_temp()
        answer_text = '오늘의 ' + temp + '입니다.'
    elif '고마워' in input_text: 
        answer_text = '별 말씀을요.'
    elif '환율' in input_text: 
        rate = exechage_rate()
        answer_text = '1달러 환율은 ' + rate + '입니다.'  
    elif '주식' in input_text: 
        price = stock(input_text)
        answer_text = price
    else: 
        answer_text = '내용을 이해하지 못했습니다.' 
    time.sleep(1)

    return answer_text

def weather_temp():
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=오늘의날씨' 
    soup = create_soup(url)
    temp = soup.find('div', attrs={'class':'temperature_text'})
    if temp: 
        temp = temp.get_text()
    else: 
        temp = '없음' 
    return temp


def exechage_rate(): 
    url='https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=환율' 
    soup = create_soup(url)
    rate = soup.find_all('span', attrs={'class':'nb_txt _pronunciation'})
    if rate: 
        rate = rate[1].get_text()
    else: 
        rate = '없음' 
    return rate

def stock(input_text): 
    index = input_text.find('주식')
    query=input_text[:index+2]
    url='https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=' + query
    soup = create_soup(url)
    price = soup.find('div', attrs={'class':'spt_tlt'}).find('span', attrs={'class':'spt_con'})
    if price: 
        price = price.get_text()
    else:
        price = '없음' 
    return price


if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000)