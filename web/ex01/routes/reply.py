from flask import Blueprint, request
from dao import replyDAO
import json

bp = Blueprint('reply', __name__, url_prefix='/reply')

@bp.route('/<int:bid>')
def list(bid):
    args = request.args
    row = replyDAO.total(bid)
    rows = replyDAO.list(bid, args)
    data = {'total':row.get('cnt'), 'list':rows}
    if rows:
        return data
    else:
        return []
    
@bp.route('', methods=["POST"])
def insert():
    req = json.loads(request.get_data())
    print(req)
    result = replyDAO.insert(req)
    return result

@bp.route('/<int:rid>', methods=['DELETE'])
def delete(rid):
    result = replyDAO.delete(rid)
    return result

@bp.route('', methods=["PUT"])
def update():
    req = json.loads(request.get_data())
    result = replyDAO.update(req)
    return result
