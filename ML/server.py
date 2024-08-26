from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.secret_key = 'mysecret'
socketio= SocketIO(app)


@app.route('/')
def index():
    return 'ㅎㅇ'




@app.route('/chat/<room>') #접속은 http://localhost:5000/chat/room?uid=blue
def chat(room):
    uid = request.args['uid']
    # //아이디와 room 이름을 session에 저장한다.
    session['uid']=uid
    session['room'] = room
    return render_template('chat.html', title='심심이', room=room)

@socketio.on('joined', namespace='/chat')
def joined(message):
    uid = session['uid']
    room = session['room']
    join_room(room)
    #클라이언트에 데이터를 송신하는 함수
    #첫 번째 인자("status"): 클라이언트에게 발생시킬 이벤트 명
    #두 번째 인자({"msg":...}): 클라이언트에게 전송한 데이터
    #세 번째 인자(room=room): 해당 이벤트를 송신할 대상 (room의 경우, 해당 그룹에 있는 세션 전체)
    emit('status', {'msg': uid + '님 입장하셨습니다.'}, room=room)

@socketio.on('left', namespace='/chat')
def left(message):
    # // 현재 세션을 room이라는 그룹 내에 제외함
    room=session['room']
    leave_room(room)
    emit('status', {'msg':session['uid'] + '님이 퇴장하셨습니다.'}, room=room)

@socketio.on('text', namespace='/chat')
def text(message):
    room = session.get('room')
    emit('message', {'msg':session.get('uid') + " : " + message['msg']}, room=room)


if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000)