import json
from flask import Blueprint, request
from dao import bbs as bbsDAO

bp = Blueprint('bbs', __name__, url_prefix='/bbs')

@bp.route('/')
def list() :
    args = request.args
    print(args.get('page'), args.get('size'))
    rows = bbsDAO.list(args)
    row = bbsDAO.total()
    return {'total':row.get('cnt'), 'list':rows}

@bp.route('/', methods=['POST'])
def insert() :
    data = json.loads(request.get_data())
    result = bbsDAO.insert(data)
    return result

@bp.route('/<int:bid>', methods=["DELETE"])
def delete(bid):
    result = bbsDAO.delete(bid)
    return result

@bp.route('/<int:bid>')
def read(bid):
    result = bbsDAO.read(bid)
    return result

@bp.route('/<int:bid>', methods=["PUT"])
def update(bid):
    data = json.loads(request.get_data())
    result = bbsDAO.update(data)
    return result