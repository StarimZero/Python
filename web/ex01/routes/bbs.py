from flask import Blueprint, render_template, request
from dao import bbsDAO
import json

bp = Blueprint('bbs', __name__, url_prefix='/bbs')

@bp.route('/')
def list():
    return render_template('index.html', title="게시판", pageName='bbs/list.html')

@bp.route('/list.json')
def listJSON():
    args = request.args
    page = args['page']
    size = args['size']
    list = bbsDAO.list(page, size)
    total =bbsDAO.total()
    data = {'total': total.get('cnt'), 'list':list}
    return data

@bp.route('/insert')
def insert():
    return render_template('index.html', title="글쓰기페이지", pageName='bbs/insert.html')

@bp.route('/insert', methods=['POST'])
def insertPost():
    req = json.loads(request.get_data())
    #print(req)
    result = bbsDAO.insert(req)
    return result

@bp.route('/<int:bbs_id>')
def read(bbs_id):
    vo=bbsDAO.read(bbs_id)
    return render_template('index.html', bbs=vo, title='게시글정보', pageName='bbs/read.html')

@bp.route('/<int:bid>', methods=['DELETE'])
def delete(bid):
    result = bbsDAO.delete(bid)
    return result

@bp.route('/update/<int:bid>')
def update(bid):
    vo=bbsDAO.read(bid)
    return render_template('index.html', bbs=vo, title="글수정페이지",  pageName='bbs/update.html')

@bp.route('', methods=['PUT'])
def updatePost():
    req = json.loads(request.get_data())
    print(req)
    result = bbsDAO.update(req)
    return result


